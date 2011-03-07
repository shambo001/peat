#!/usr/bin/env python
#
# Protein Engineering Analysis Tool DataBase (PEATDB)
# Copyright (C) 2010 Damien Farrell & Jens Erik Nielsen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Email: Jens.Nielsen_at_gmail.com 
# Normal mail:
# Jens Nielsen
# SBBS, Conway Institute
# University College Dublin
# Dublin 4, Ireland
# 
# Author: Damien Farrell 2011

"""This script will create multiple projects from csv files and
add pdbs based on the csv names. It can also create peatsa jobs
and merge them back into the database"""

import pickle, sys, os, copy, time, types, math
import numpy
from PEATDB.Base import PDatabase 
from PEATDB import Utils
from PEATDB.Actions import DBActions
from PEATDB.plugins.PEATSAplugin import PEATSAPlugin
from PEATDB.plugins.Correlation import CorrelationAnalyser
from PEATDB.PEATTables import PEATTableModel
import PEATDB.Utils
from PEATDB.Parsers import XMLParser
import matplotlib.pyplot as plt
from scipy.stats import stats

#plt.rc('text',usetex=True)
plt.rc('font',size=7)
plt.rc('legend',fontsize=6)
plt.rc('savefig',dpi=300)
plt.rc('axes',linewidth=.5)

settings={'server':'peat.ucd.ie','username':'guest',
           'password':'123'}
path = '/home/people/farrell/Desktop/SADBPaperData'
savepath = os.path.join(path,'projects')
cpath = os.path.join(path,'data')
csvfiles = os.listdir(cpath)#[:4]
dbnames = [os.path.splitext(i)[0] for i in csvfiles]
print dbnames

def getPDBXML(name):
    url = 'http://www.rcsb.org/pdb/rest/describePDB?structureId=%s' %name
    p = XMLParser()
    d = p.openurl(url)    
    return d['PDB']

def PEATSAJobs(prjs):
    """Submit PEATSA runs for all projects or merge results if done"""
    for name in prjs:
        print name
        DB = PDatabase(local=os.path.join(savepath,name))
        pdb = DB['wt'].Structure
        PS = PEATSAPlugin()
        PS.main(DB=DB)        
        if hasattr(DB.meta,'peatsa_jobs'):
            if 'mycalc' in DB.meta.peatsa_jobs:
                print 'job already present'
                #try to merge results
                S = PEATTableModel(DB)
                job,n = PS.getJob('mycalc')
                PS.mergeResults(job, 'prediction', S)
                DB.commit()
                print 'merged results'
        else:
            mutlist = []
            for p in DB.getRecs():
                mutlist.append(DB.get(p).Mutations)
            #print mutlist
            pdbfile = PS.writetempPDB()
            PS.submitJob(name='mycalc', pdbname=DB.meta.refprotein, pdbfile=pdbfile, 
                         mutations=mutlist, calcs=['stability'], meta={'protein':name})
            #required to end process
        PS.jobManager.stopLogging()
        DB.close()
    return

def createProjects(files):
    """Create multiple projects at once from csv files"""

    for filename in files:
        print filename
        name = os.path.splitext(filename)[0]
        #create/open db
        DB = PDatabase(local=os.path.join(savepath,name))
        DB.add('wt')
        #add wt pdb
        stream = DBActions.fetchPDB(name)
        DBActions.addPDBFile(DB, 'wt', pdbdata=stream, pdbname=name, gui=False)
        DB.meta.refprotein = 'wt'
        DB.meta.info['protein'] = name
        #import data from csv
        DB.importCSV(os.path.join(cpath,filename), namefield='Mutations')
        print 'imported ok'
        DB.deleteField('PDB')
        DB.commit()
        DB.close()
        print 'done'
    return

def summarise(projects):
    summDB = PDatabase(local='summary.fs')
    C = CorrelationAnalyser()
    figs = []
    for f in range(3):
        figs.append(plt.figure())
    
    import matplotlib.gridspec as gridspec
    gs = gridspec.GridSpec(5, 5, wspace=0.3, hspace=0.5)    
    i=0
    data=[]
    for p in projects:
        print p
        DB = PDatabase(local=os.path.join(savepath,p))
        S = PEATTableModel(DB)
        #print DB.meta.info
        try:
            exp,pre = S.getColumns(['Exp','prediction'],allowempty=False)
            errs = [j[0]-j[1] for j in zip(exp,pre)]
        except:
            print 'no results'
            continue
        cc,rmse,meanerr = C.getStats(pre,exp)
        #ttest for mean errs 0        
        ttp = round(stats.ttest_1samp(errs, 0)[1],2)
        #normality of errs
        w,swp = C.ShapiroWilk(errs)
        ax = figs[0].add_subplot(gs[0, i])
        C.plotCorrelation(pre,exp,title=p,ms=2,axeslabels=False,ax=ax)
        ax = figs[1].add_subplot(gs[0, i])
        C.showHistogram([pre,exp],title=p,labels=['pre','exp'],ax=ax)                
        ax = figs[2].add_subplot(gs[0, i])
        C.plotNorm(errs,title=p,lw=1,ax=ax)
        x={'name':p,'rmse':rmse,'corrcoef':cc,'meanerr':meanerr,
           'ttest':ttp,'shapirowilk':swp}
        print x
        pd = getPDBXML(p)
        x.update(pd)
        data.append(x)
        i+=1
    
    summDB.importDict(data)
    #summDB.commit()
    for i in range(len(figs)):
        figs[i].savefig('fig%s.png' %i)
    #plt.show()
    return

def send2Server():
    settings={'server':'peat.ucd.ie','username':'guest',
               'password':'123','port':8080}
    DB = PDatabase(local='summary.fs')    
    Utils.copyDBtoServer(DB,'PEATSAmultiprojects',settings)
    return
    
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()    
    parser.add_option("-i", "--importcsv", dest="importcsv", action='store_true',
                       help="create/import", default=False)
    parser.add_option("-j", "--jobs", dest="jobs", action='store_true',
                       help="do/merge jobs", default=False)
    parser.add_option("-s", "--summary", dest="summary", action='store_true',
                       help="do summary", default=False)
    parser.add_option("-p", "--path", dest="path",
                        help="Path with csv files")
    parser.add_option("-c", "--copy", dest="copy",action='store_true',
                        help="copy to server", default=False)   
    opts, remainder = parser.parse_args()

    if opts.path != None:
        print path
    if opts.importcsv == True:
        createProjects(csvfiles)
    if opts.jobs == True:    
        PEATSAJobs(dbnames)
    if opts.summary == True:
        summarise(dbnames)
    if opts.copy == True:
        send2Server()
  
