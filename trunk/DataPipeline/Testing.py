#!/usr/bin/env python
#
# DataPipeline - A data import and fitting tool
# Copyright (C) 2011 Damien Farrell
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
# Email: damien.farrell_at_ucd.ie
# Normal mail:
# Damien Farrell
# SBBS, Conway Institute
# University College Dublin
# Dublin 4, Ireland
#

"""Tests for data pipeline."""
from Base import Pipeline
import os, random, time, string
import numpy as np
from math import *
import csv
from PEATDB.Ekin.Base import EkinProject

class Tester(object):
    """This class does all the pipeline tests"""

    basictests = {'test1':({'format':'databyrow','model1':'Linear'},'databyrow1.txt'),
                  'test2':({'format':'databycolumn'},'databycol1.txt'),
                  #rows, multiple groups
                  'test3':({'format':'databyrow','colrepeat':6},'databyrow2.txt'),
                  #cols, multiple groups
                  'test4':({'format':'databycolumn','rowrepeat':6},'databycol2.txt'),
                  #paired x-y data in rows
                  'test5':({'format':'paireddatabyrow'},'databyrow_paired.txt'),
                  #paired x-y data in cols
                  'test6':({'format':'paireddatabycolumn'},'databycol_paired.txt'),
                  #various non-default formatting
                  'test7':({'format':'databyrow','delimeter':'tab','decimalsymbol':',',
                            'colrepeat':6}, 'databyrow_errors.txt'),
                  #fitting models included
                  'test8':({'format':'groupeddatabyrow','rowrepeat':4,'rowheader':0,'rowstart':1,
                             'model1':'Linear'}, 'databyrow_grouped.txt'),
                  'test9':({'format':'groupeddatabycolumn','colrepeat':4,'colheader':0,'colstart':1,
                            'model1':'Linear','model2':'sigmoid','variable1':'a','variable2':'tm',
                            'xerror':0.2,'yerror':0.3},
                            'databycol_grouped.txt'),
                  #'test10':({'format':'databyrow','rowheader':"aaa,bbb,ccc,ddd"},
                  #          'databyrow_noheader.txt')
                  }

    exceltests = {'test1':{'conf':{'format':'databyrow'},
                           'filename':'databyrow1.xls'}}

    def doTest(self, info, name='test', path='testfiles'):
        p = Pipeline()
        conf = info[0]
        filename = info[1]
        p.createConfig('temp.conf',**conf)
        p.openRaw(os.path.join(path,filename))
        #data = p.doImport()
        p.run()
        print '%s completed' %name
        print '-------------------'

    def formatTests(self, testinfo):
        """Test basic standard format handling"""
        for t in sorted(testinfo.keys()):
            self.doTest(testinfo[t], t)
    
    def multiFileTests(self):
        """Tests the processing and grouping of multiple files"""
        pth = 'testfiles/group1'
        self.createGroupedData1(pth)
        conf = {'format':'databycolumn','groupbyfile':1, 'parsenumericvalues':1,
                'parsevaluesindex':0,'saveplots':1,
                'model1':'linear','variable1':'a','model2':'sigmoid','variable2':'tm'}
        p = Pipeline()
        p.createConfig('temp.conf',**conf)
        p.addFolder(pth, ext='txt')
        p.run()
        return
    
    def fitPropagationTest(self):
        """Tests the propagation of fit data direct from a dict - no importing"""
    
        start=time.time()
        p = Pipeline()
        conf = {'model1':'linear','model2':'Michaelis-Menten','model3':'sigmoid',
                'variable1':'a','variable2':'Km','variable3':'tm',#'xerror':.1,'yerror':0.05,
                'saveplots':1}
        p.createConfig('temp.conf',**conf)
        data = self.createNestedData()
        Em = EkinProject()    
        E,fits = p.processFits(data, Em=Em)
        print 'final fits', fits
        fname = os.path.join(p.workingdir,'results')
        Em.saveProject(fname)
        p.saveEkinPlotstoImages(Em, fname)
        print 'completed fit propagation test'
        print 'took %s seconds' %round((time.time()-start),2)
        print '-------------------'
        return 
        
    def customTests(self):
        """Tests kinetics data for paper"""
    
        info = ({'format':'kineticsdata','colrepeat':4,'colheader':0,'colstart':1,
                  'model1':'Linear'},'setG_110309_1_pH7,5.txt')
        doTest(info, 'kinetics test', 'novo_setG/rep1')
    
    def createGroupedData1(self, path='testfiles'):
        """Create sets of fake data to test queuing and file grouping"""
        
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            Pipeline.clearDirectory(path)
        names = []
        for n in range(10):    
            l=''.join(random.choice(string.ascii_uppercase) for x in range(6))
            names.append(l)
        print names
        for i in np.arange(2,10,1.0):
            #fname = os.path.join(path,'ph_'+str(i)+'.txt')
            fname = os.path.join(path,'ph_'+str(i)+'__xx_'+str(i*3)+'.txt')
            cw = csv.writer(open(fname,'w'))
            cw.writerow(['temp']+names)
            for x in range(250,360,2):
                vals = [round(i*x/random.normalvariate(10,0.3),2) for j in range(len(names))]
                vals.insert(0,x)
                cw.writerow(vals)
        return
        
    def createNestedData(self):
        """Create simulated nested data similar to our kinetics data"""
        data={}
        names = ['aaa','bbb','ccc']
        tms = [7.5,8.0,8.5]
        phs = range(2,14) #e.g. a ph range
        concs = [0.01,0.1,0.2,0.3,0.5,1.0,2.0,5.0]
        x = range(0,100,10)
    
        for n in names:
            i=names.index(n)
            tm=tms[i]#+random.normalvariate(0,0.1)
            data[n]={}
            for p in phs:
                km = 2/(1+exp((p-tm)/1.2))
                #print p,km
                data[n][p]={}
                for s in concs:
                    vel = (10 * s)/(s + km)
                    y = [round(i*vel,3) for i in x]
                    y = [i * random.normalvariate(1,0.03) for i in y]
                    data[n][p][s] = (x,y)    
        return data

def main():
    t=Tester()
    #t.formatTests(t.basictests)
    #t.customTests()
    t.multiFileTests()
    #t.fitPropagationTest()
    
if __name__ == '__main__':
    main()
