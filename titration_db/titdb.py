#!/bin/env python
#
#
# This file is part Protein Engineering Analysis Tool (PEAT)
# (C) Copyright Jens Erik Nielsen, University College Dublin 2003-
# All rights reserved
#
#
# Rewritten by D Farrell, Jan 2009
#

import cgi
import sys,os, string, types
os.environ['MPLCONFIGDIR']='/tmp'
from PEATDB.Base import PDatabase
from PEATDB.Record import PEATRecord
from PEATDB.PEATTables import PEATTableModel, PEATTable
from PEATDB.web import PEATWeb
from pKD import pKDInterface

class titdbWeb(PEATWeb):

    """Class providing a web interface for PEAT projects subclassed for titration_db"""

    def __init__(self, server='localhost', project='test', port=8080,
                        user=None, passwd=None,
                        bindir='', fullpath=''):
    
        """bindir : path to cgi script in server address
           fullpath : file system path to script  """

        import socket
        self.host = socket.getfqdn(socket.gethostname())

        self.sessionkey=None
        self.form=cgi.FieldStorage()
        self.server = server
        self.project = project
        self.user = user
        self.password = passwd
	self.port = port
        
        self.bindir = bindir
	dirname = os.path.basename(fullpath)
        self.imgdir = '/' + dirname + '/images'
        self.plotsdir = '/'+ dirname + '/plots'
        self.imagepath = fullpath + '/plots'

        action = self.form.getfirst('action')
        self.action = action
        if not self.form.getfirst('action'):
            self.show_intro()
            return
        elif action == 'show_intro':
            self.show_intro()
        elif action == 'show_help':
            self.show_help()
        elif action == 'summary':
            self.showSummary()
        elif action == 'analysis':
            self.showAnalysis()
        elif action == 'show_all':
            self.show_all()
        elif action=='show_specific':
            self.show_specific()
        elif action == 'show_datasets':
            self.show_datasets()
        elif action == 'search':
            self.show_search_results()
        elif action == 'selectpKD':
            self.selectpKD()
        elif action == 'showpKD':
            self.showpKD()

        return

    def show_intro(self):
        '''Show intro page'''
        self.show_DB_header(menu=1)

        print '<div align=left>'
        print '<big><big><a>Welcome to the protein pH titration database (Beta).</big></a>'
        print '<br>'
        print '<br>'
        print '<a>This web site provides raw NMR titration curves obtained from published sources. \
                This web interface is designed to provide the following services:</a>'
        print '<UL>\
                <LI>Browse contents of the DB in one table\
                <LI>Search for curves based on residue name, pka values, residue type etc.\
                <LI>Visualise and overlay any combination of curves (and our fits)\
                <LI>View some summary statistics on the current dataset\
                <LI>Download the raw data as csv/text files and refit/analyse\
                </UL>'

        print '<a>If you wish to submit data to be included here, we currently recommend that you\
                send the tabulated data (or even plotted curve images) by mail to us at</a> \
                <a href="mailto:damien.farrell@ucd.ie"> this address</a><p>'
        print '<a> Alternatively, you may submit the data to the database using our PEAT\
                software. Download PEAT at </a> <a href="http://enzyme.ucd.ie/PEAT" > http://enzyme.ucd.ie/PEAT</a><br><br>'
        #print '</table>'
        print '</div>'
        self.footer()
        return

    def show_help(self):
        '''Show help page'''
        self.show_DB_header(menu=1)

        print '<div align=left>'
        print '<h2>Help information for using these pages is available <a href="http://enzyme.ucd.ie/main/index.php/Titration_DB"> here</a></h2>'
        print '<h3>Please report any bugs or requests for improvements to <a href="mailto:damien.farrell@ucd.ie"> this address </a><br><br>'
        print 'You may cite this database using the following reference:</h3>'
        print '<b>Farrell, D., et al., Titration_DB: Storage and analysis of NMR-monitored protein pH titration curves.<br>'
        print 'Proteins: Structure, Function, and Bioinformatics, 2009. In press. DOI: 10.1002/prot.22611</b>'
        print '<a href="http://www3.interscience.wiley.com/journal/122593997/abstract"> link </a>'
        print '</div>'

        self.footer()

        return


    def show_DB_header(self,title=None,menu=None):
        """show headings and column names for DB"""

        imgdir = self.imgdir
        html_header = 'Content-Type: text/html; charset=utf-8\n'
        html_header += '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/loose.dtd">\n\n'
        print html_header
        print '<html>'
        print '<head>'

        if title==None:
            print '<title>Protein Titration Database</title>'
        else:
            print '<title>%s</title>' % title
        print '<link href="http://%s/titration_db/styles.css" rel="stylesheet" type="text/css" />' %self.host
        print '<link rel="shortcut icon" href="http://%s/titration_db/favicon.ico" type="image/x-icon" />' %self.host
        print '<script type="text/javascript" src="/scripts/checkbox.js"></script>'
        print '</head>'
        print '<body>'
        print '<div class="header">'
        print '<img src="%s/titDB_logo.png" align=LEFT>' %imgdir
        print '<img src="%s/banner_icon.png" style="float: right; padding-right:5;">' %imgdir
        print '<p id="title">:an NMR protein titration database</p>'

        print '</div>'
        print '<script type="text/javascript" src="/scripts/boxover.js"></script>'
        print '<hr>'
        print '<div>'

        if menu==1:
            self.menu()

        return

    def footer(self):
        """Print page footer"""

        print '<br>'
        print '<p><center>Provided by <a href="http://enzyme.ucd.ie">Nielsen Research Group at UCD</a></center></p>'
        print '<p><center>Supported by <a href="http://www.sfi.ie">Science Foundation Ireland</a></center></p>'
        print '<center><a href="http://www.sfi.ie"><img src="%s/sfi_logo.png" border="0"></a></center></p>' %self.imgdir

        print '</div>'
        print '</div>'
        print '</body>'
        return

    def menu(self):
        """Print the menu"""
	#print bindir
	bindir = self.bindir
        print '<div class="menu">'
        print '<table id="menu" valign=top align=left>'
        print '<th><b>Menu</b></th>'

        print '<form action="%s/main.cgi" METHOD="POST" ENCTYPE="multipart/form-data">' %bindir
        self.write_sessionkey('show_intro')
        print '<tr><td class="menu">\
            <input type=submit value="Home" name=submit size=20 class="btn"></td></tr>'
        print '</form>'
        print
        print '<form action="%s/main.cgi" METHOD="POST" ENCTYPE="multipart/form-data">'  %bindir
        self.write_sessionkey('show_all')
        print '<tr><td class="menu">'
        print '<input type=submit value="Show All Records" name=submit class="btn"'
        print """title="header=[Show all] body=[Show all records in the DB]"></td></tr>"""
        print '</form>'

        print
        print '<form action="%s/main.cgi" METHOD="POST" ENCTYPE="multipart/form-data">' %bindir
        self.write_sessionkey('summary')
        print '<tr><td class="menu">\
            <input type=submit value="Summary" name=submit class="btn"></td></tr>'
        print '</form>'

        print
        print '<form action="%s/main.cgi" METHOD="POST" ENCTYPE="multipart/form-data">' %bindir
        self.write_sessionkey('analysis')
        print '<tr><td class="menu">\
            <input type=submit value="Analysis" name=submit class="btn"></td></tr>'
        print '</form>'

        print '<form action="%s/main.cgi" METHOD="POST" ENCTYPE="multipart/form-data">' %bindir
        self.write_sessionkey('selectpKD')
        print """<tr><td class="menu">\
             <input type=submit value="pKD" name=submit class="btn"\
             title="header=[Refresh] body=[Cross reference curves with calculated data from pKD server<br>\
             <img src=http://enzyme.ucd.ie/pKD/slide8.bmp width=150>]"></td></tr>""" 

        print '</form>'
        print

        print '<form action="%s/main.cgi" METHOD="POST" ENCTYPE="multipart/form-data">' %bindir
        self.write_sessionkey('show_help')
        print '<tr><td class="menu">\
            <input type=submit value="Help" name=submit class="btn"></td></tr>'
        print '</form>'
        print

        searchmessage = 'Enter your search here'
        print '<tr><td class="menu"><a><b>SEARCH</a></td></tr>'
        print '<form action="%s/main.cgi" METHOD="POST" ENCTYPE="multipart/form-data">' %bindir
        self.write_sessionkey('search')
        #protein search box
        print '<tr><td class="menu">'
        print 'Protein: '
        print '<select name="proteinmatchmethod" class="btn">'
        print '<option value="or">Any words'
        print '<option value="and">All words'
        print '</select>'
        print '</td></tr>'
        print '<td class="menu">'
        print """<input type="text" name="words" size=22 maxlength=50 value="" \
                title="header=[Protein search] body=[Enter multiple names seperated by a space.\
                    This search is not case sensitive]"></td></tr>"""

        #residue search box
        print '<tr><td class="menu">'
        print 'Residue: '
        print '<tr><td class="menu">'
        print """<input type="text" name="residue" size=22 maxlength=40 value="" class="btn"\
                 title="header=[Residue type] body=[Use three letter codes, e.g. GLU ASP LYS]"></td></tr>"""
        #pka search box
        print """<tr><td class="menu"> pKa range: <input type="text" name="pka" size=22 \
                maxlength=30 value="" title="header=[pKa range] body=[Enter a range of values using \
                this format: e.g. 5-6]"></td></tr>"""

        #nucleus search box
        print '<tr><td class="menu">'
        print 'Nucleus: <select name="nucleus" class="btn">'
        print '<option value="any">Any'
        print '<option value="1H">1H'
        print '<option value="15N">15N'
        print '<option value="13C">13C'
        print '</select>'
        print '</td></tr>'

        #drop list for whether to match any or all of the searches from each box
        print '<tr><td class="menu">'
        print """Match: <select name="matchmethod" class="btn" title="header=[Global match method] \
                 body=[Match records with ALL of the search criteria or only those with ANY those\
                  attributes]">"""
        print '<option value="and">All'
        print '<option value="or">Any'
        print '</select> <p>'
        print '</td></tr>'
        print '</td></tr>'
        print '<tr><td class="menu"><input type="submit" value="Search Now" class="btn"></td></tr>'
        print '</form>'
        print '</table>'
        print '</div>'
        print '<div id="content">'
        return

    def showSummary(self):
        from PEATDB.Ekin.Titration import TitrationAnalyser
        self.show_DB_header(menu=1)
        DB = self.DB = self.connect()      
        sys.stdout.flush()        
        t = TitrationAnalyser()
        ekindata = t.getEkinDicts(DB)
        t.dotitDBStats(ekindata)
        return

    def showAnalysis(self):
        """Analysis of current pKas"""
        from PEATDB.Ekin.Titration import TitrationAnalyser
        self.show_DB_header(menu=1)
        DB = self.DB = self.connect()
        sys.stdout.flush()
     
        t = TitrationAnalyser()
        colnames = ['1H NMR','15N NMR','13C NMR']

        for col in colnames:	    
            p = t.extractpKas(DB,col,silent=True)	     
            print '<div>'
            print "<h2>%s: Table of fitted 'reliable' pKas and distribution of associated &Delta;&delta;</h2>" %col
            img1, img2 = t.analysepKas(p, silent=True, prefix=col, path=self.imagepath)
            t.makepKasTable(p)
            print '<center><img src="%s/%s" align=center></center>' %(self.plotsdir, img2)
            print '<div>'
            print '<hr>'
        self.footer()
        return

 
    def do_search(self, globalop, proteinop, proteins, residues, nucleus, pka):
        """Do searches for the various parameters, name, pka etc"""

        import re, urllib
        from PEATDB.PEATTables import PEATTableModel
        from PEATDB.Ekin.Fitting import Fitting
        from PEATDB.Ekin.Web import EkinWeb
        DB = self.DB  
        EW = EkinWeb()
        ekincols = DB.ekintypes

        found=[]
        protlist = proteins.split(' ')
        residuelist = residues.split(' ')

        def createPhrase(items, op):
            if op == 'or':
                logicsymbol = '|'
            else:
                logicsymbol = '+'
            itemlist = items.split(' ')
            phrase =''
            c=1
            for i in itemlist:
                if c == len(itemlist):
                    phrase = phrase + i
                else:
                    phrase = phrase + i + logicsymbol
                c=c+1
            return re.compile(phrase, re.IGNORECASE)

        #if there is a protein name entered, get the list of proteins/records to use
        #otherwise use all records to search for the other keys
        names = []
        keywords = {}
        for p in DB.getRecs():
            name = DB[p].name
            names.append((name,p))
            if hasattr(DB[p], 'keywords'):
                keywords[name] = DB[p].keywords
            else:
                keywords[name] = ''
        names.sort()

        #create search expressions
        s_protein = createPhrase(proteins, proteinop)
        s_residue = createPhrase(residues, 'or')
        pkarange = pka.split('-')

        #do search
        for name in names:
            proteinname = name[0]
            protein = name[1]
            if s_protein.search(proteinname) or s_protein.search(keywords[proteinname]):
                found.append(protein)

        if len(found)==0:
            print '<h2>Sorry, no proteins found that match this name. <h2>'
            return
        elif residues == '' and pka == '':
            self.show_DB(selected=found)
            return found

        #now search for the other keys inside selected proteins if needed
        ekinfound={}; foundfits={}
        ignore =['__fit_matches__', '__Exp_Meta_Dat__', '__datatabs_fits__']
        
        kys = list(DB.getRecs())
        kys.sort()
        if len(found) == 0 or globalop == 'or':
            found = DB.getRecs()

        print '<table id="mytable" cellspacing=0 align=center>'
        '''search recs for residue and pkarange
           and add dataset names to new ekinfound dict'''
        for protein in found:
            for col in DB[protein].keys():
                if nucleus != 'any':
                    if nucleus not in col:
                        continue
                E = DB[protein][col]
                if DB['userfields'].has_key(col):
                    fieldtype=DB['userfields'][col]['field_type']
                else:
                    fieldtype=None
                if fieldtype in ekincols:
                    dk = E.datasets                    
                    fits = E.__datatabs_fits__                    
                    for k in dk:
                        meta = E.getMetaData(k)
                        try:
                            thisres = meta['residue']
                        except:
                            thisres = k         
                        if thisres == None:
                            thisres = k
                        if residues != '':
                            if s_residue.search(thisres) and not k in ignore:
                                if not ekinfound.has_key(protein+'$'+col):
                                    ekinfound[protein+'$'+col]=[]
                                ekinfound[protein+'$'+col].append(k)

                        if pka != '':
                            foundpka = 0
                            if k in fits.keys():
                                if fits[k] == None:
                                    continue
                                if fits[k].has_key('model'):
                                    model = fits[k]['model']
                                else:
                                    continue
                                if not foundfits.has_key(protein+'$'+col):
                                    foundfits[protein+'$'+col]={}
                                X = Fitting.getFitter(model)
                                pnames = X.names
                                i=0
                                #check if first num is larger, then swap
                                try:
                                    pk1=float(pkarange[0])
                                    pk2=float(pkarange[1])
                                except:
                                    print '<h2> Error: pka values are not valid </h2>'
                                    return
                                if pk1 > pk2:
                                    tmp = pk1
                                    pk1 = pk2
                                    pk2 = tmp

                                #iterate thru parameter names and match any pK fields
                                #this code is not that efficient!
                                for p in pnames:
                                    if 'pK' in p:
                                        pka = fits[k][i]
                                        if pka >= pk1 and pka <= pk2:
                                            foundpka=1
                                    i=i+1
                                #if match is 'ANY', just append dataset if not there already
                                #also for case if no residue value entered
                                if globalop == 'or' or residues == '':
                                    if foundpka == 1:
                                        if not ekinfound.has_key(protein+'$'+col):
                                            ekinfound[protein+'$'+col]=[]
                                        if not k in ekinfound[protein+'$'+col]:
                                            ekinfound[protein+'$'+col].append(k)
                                #if match is 'ALL', need to check dataset already found
                                #and if no pka found, remove it. if both are true keep it
                                elif globalop == 'and':
                                    if foundpka == 0:
                                        if ekinfound.has_key(protein+'$'+col) and k in ekinfound[protein+'$'+col]:
                                            #print 'removing', protein, col
                                            ekinfound[protein+'$'+col].remove(k)

                                foundfits[protein+'$'+col][k]=fits[k]
        #check for empty fields in ekinfound dict and delete them..
        for d in ekinfound.keys():
            if len(ekinfound[d])==0:
                del(ekinfound[d])

        #if no results, just say that and return
        if len(ekinfound)==0:
            print '<h2> Sorry, no records found that match these parameters. </h2>'
            return
        #top display button and options
        print '<form name="resultsform" action="%s/main.cgi" METHOD="POST" ENCTYPE="multipart/form-data">' %self.bindir
        self.write_sessionkey('show_datasets')
        print '<td valign=top align=right colspan=3> <input type=submit value="display selected" name=submit>'
        print '<label><input type=checkbox name="plotoption" value=3>single graph</label>'
        print '<label><input type=checkbox name="normalise" value=1>normalise</label>'
        print '<label><input type=checkbox name="logx" value=1>log-x</label>'
        print '<label><input type=checkbox name="logy" value=1>log-y</label>'
        print '<label><input type=checkbox name="legend" value=1>legend</label>'
        print '<input type=button value="Check All" onClick="checkAll(document.resultsform.residue)">'
        print '<input type=button value="Uncheck All" onClick="uncheckAll(document.resultsform.residue)"></td>'
        print '</tr>'
        #header
        cols=['protein','column','residues']
        for c in cols:
            print '<th>'+c+'</th>'
        print '</tr>'
        ekys = ekinfound.keys()
        ekys.sort()

        r=1
        for k in ekys:
            if r % 2 == 0:
                cls = "spec"
            else:
                cls = ""

            fields = k.split('$')
            protein = fields[0]
            column = fields[1]

            proteinname = DB[protein]['name']
            print '<tr>'
            print '<th class="spec">%s</th> <td> %s </td>' %(proteinname, column)
            print '<td>'
            for residue in ekinfound[k]:
                residuefield = k+"$"+residue
                fithtml = ''
                try:
                    print '<input type=checkbox id="residue" name="residue" value=%s>' %("'"+residuefield+"'")
                except:
                    print 'UnicodeEncodeError'
                    continue

                urlfields = urllib.urlencode({'login':self.user,'project':self.project,
                                           'residue': residuefield,'action': 'show_datasets'})
                print '<a href="/cgi-bin/titration_db/main.cgi?%s" target="_blank">%s</a>'\
                          % (urlfields, residue)

            print '</tr>'
            r=r+1
        print '</form>'
        print '</table>'
        self.footer()

        return

    def show_search_results(self):
        """Display search results"""

        self.show_DB_header(menu=1)
        sys.stdout.flush()
        self.DB = self.connect()
       
        key=self.form.getfirst('key')
        matchmethod=self.form.getfirst('matchmethod')
        proteinmatchmethod=self.form.getfirst('proteinmatchmethod')
        words=self.form.getfirst('words')
        residue=self.form.getfirst('residue')
        nucleus=self.form.getfirst('nucleus')
        pka=self.form.getfirst('pka')

        print '<table bgcolor=#CD9B9B border="1" bordercolor=black cellspacing=0 cellpadding=4 valign=top \
                align=center width=80%><tr><td>'

        print '<div align=left>'
        print '<big><a>Search results for protein=%s %s residue=%s %s nucleus=%s pka=%s</big></a>'\
                  %(words,matchmethod,residue,matchmethod,nucleus,pka)
        print '<br>'
        print '</div>'
        print '</table>'
        self.do_search(matchmethod, proteinmatchmethod, words, residue, nucleus, pka)
        return

    def selectpKD(self):
        """Allow user to select a protein and field for pKD"""

        self.show_DB_header(menu=1)
        sys.stdout.flush()
        DB = self.DB = self.connect()        

        names = []
        for p in DB.getRecs():
            names.append((DB[p].name,p))
        names.sort()
        nucl = ['1H NMR', '15N NMR', '13C NMR']

        #check pKD available calcs
        P = pKDInterface()
        pkdprots = [string.upper(e[0]) for e in P.getProteins()]

        #add selection boxes
        print '<div align=left>'
        print '<form name="pkdform" action="%s/main.cgi" METHOD="POST" ENCTYPE="multipart/form-data">' %self.bindir
        self.write_sessionkey('showpKD')

        print '<big>Select experimental curves to compare with calculated curves in pKD</big><br>'
        print '<a>This will show a set of plots for each residue where there is an experimental and calculated curve</a><p>'
        print 'Choose the protein and nucleus:<p>'
        print '<select name="protein" class="btn">'
        for n in names:
            print '<option value="%s">%s</option>' %(n[1],n[0])
        print '</select>'
        print '<select name="column" class="btn">'
        for c in nucl:
            print '<option value="%s">%s</option>' %(c,c)
        print '</select>'
        print '<p>'
        #button
        print '<input type=submit value="Display Plots" name=submit class="btn">'
        print '<label><input type=radio name="option" value=1 checked="yes">compare both</label>'
        print '<label><input type=radio name="option" value=2>exp only</label>'
        print '<label><input type=radio name="option" value=3>calcs only</label>'
        print '</form>'

        print '</div>'
        print 'Below is a reference table showing which proteins in our DB currently have calculations in the pKD, with the PDB ID and PDB link.<br>'
        print 'If the protein is not yet available, you can go to <a href=http://enzyme.ucd.ie/cgi-bin/pKD/server_start.cgi target="blank"> \
                    the pKD page</a> and submit the calculation.<p>'
        #table of proteins and their PDBs
        print '<div align=left>'
        print '<table id="mytable" cellspacing="0">'
        r=0
        print '<th>Protein</th><th>PDB</th><th>Has pKD data</th>'
        for name in names:
            protein = name[1]
            protname = name[0]
            if not DB[protein].has_key('PDB_link'):
                continue
            pdbinfo = DB[protein].PDB_link
            if pdbinfo == '':
                continue
            pdbid = pdbinfo['text']
            pdblink = pdbinfo['link']
            if r % 2 == 0:
                cls = 'alt'
            else:
                cls = ''
            print '<tr>'
            print '<td class=%s> %s </td>' % (cls, protname)
            print '<td class=%s> <a href=%s target="blank"> %s</a> </td>' % (cls, pdblink, pdbid)
            if pdbid in pkdprots:
                status = 'yes'
            else:
                status = 'no'
            print '<td class=%s> <b>%s</b> </td>' %(cls, status)
            print '</tr>'
            r=r+1
        print '</table>'
        return

    def showpKD(self):
        """Show pKD calcs with exp data for selected ekindata"""
        protein = self.form.getfirst('protein')
        col = self.form.getfirst('column')
        showopt = self.form.getfirst('option')

        self.show_DB_header(menu=1)
        sys.stdout.flush()
        DB = self.DB = self.connect()        
        protname = DB[protein]['name']
        pdbid = DB[protein]['PDB_link']['text']
        expdata = DB[protein][col]
        if type(expdata) is types.StringType:
            print '<a>No data for column %s, go back and choose another nucleus..</a>' %col
            return

        P = pKDInterface()
        calcs, pkas, pdblines = P.loadfrompKD(pdbid)

        print '<div><a>Protein: %s PDB: %s </a><br>' %(protname, pdbid)
        print 'Column data: %s <p></div>' %col
        if calcs == None or not type(calcs) is types.DictType:
            print '<a>There are currently no pKD calculations for this protein.</a>'
            return
        else:
            print '<a>Found data on pKD server. We can plot.</a>'
            sys.stdout.flush()
        #plot them
        self.plotpKDCalcs(calcs, expdata, showopt)
        self.footer()
        return


    def plotpKDCalcs(self, calcs, Ed=None, option=1):
        """Do pKD calcs with exp data plots"""
        from PEATDB.Ekin.Web import EkinWeb
        from PEATDB.Ekin.Base import EkinProject
        from PEATDB.Ekin.Convert import EkinConvert
        from PEATDB.Ekin.Titration import TitrationAnalyser
        import PEATDB.Ekin.Utils as Utils
        t = TitrationAnalyser()
        c=calcs
        
        EW = EkinWeb()

        if option == '2':
            print '<a>Just showing experimental data</a>'
            EW.showEkinPlots(project=Ed, datasets='ALL',
                              path=self.plotsdir,
                              imgpath=self.imagepath)
            return
        #create ekin proj from pKD titcurves
        Ec = EkinProject()
        for r in c.keys():
            xd=[];yd=[]
            for i in c[r]:
                if type(i) is types.StringType:
                    continue
                xd.append(i)
                yd.append(c[r][i])
            edata=EkinConvert.xy2ekin([xd,yd])
            Ec.insertDataset(edata, r)

        print '<a>Please wait, fitting calcated curves...</a>'
        sys.stdout.flush()
        Ec.fitDatasets(models=['1 pKa 2 Chemical shifts'], silent=True)

        if option == '3':
            print '<a>Just showing pKD data</a>'
            EW.showEkinPlots(project=Ec, datasets='ALL',
                              path=self.plotsdir,                              
                              imgpath=self.imagepath)
            return            

        #transform exp data names to match pKD ones
        s=':'
        usechainid = True
        #if pKD names have no chain id, we don't need one for exp names
        if Ec.datasets[0].startswith(':'):
            usechainid=False
        for d in Ed.datasets[:]:            
            r = Ed.getMetaData(d)
            if r != None:
                if r['chain_id'] == None or usechainid == False:
                    chain = ''
                else:
                    chain = r['chain_id']
                new = chain+s+Utils.leadingZeros(r['res_num'],4)+s+r['residue']
                if new in Ed.datasets:
                    atom = r['atom']
                    new = new + '_' + atom
                Ed.renameDataset(d, new)

        #now we overlay the same datasets in Ed and Ec
        #also handles cases where same residue multiple times for diff atoms in exp data
        for d in Ed.datasets:
            if d in Ec.datasets:
                Ep = EkinProject()
                cdata = Ec.getDataset(d)
                Ep.insertDataset(cdata, d+'_pKD')
                Ep.setFitData(d+'_pKD', Ec.getFitData(d))
                ddata = Ed.getDataset(d)
                Ep.insertDataset(ddata, d+'_exp')
                Ep.setFitData(d+'_exp', Ed.getFitData(d))
                EW.showEkinPlots(project=Ep, datasets='ALL', plotoption=3,
                                 normalise=True, legend=True,
                                 path=self.plotsdir,
                                 imgpath=self.imagepath)

        return

if __name__ == '__main__':
    PEATWeb()
