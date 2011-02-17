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

from Tkinter import *

#import matplotlib
import matplotlib.pyplot as plt
import pylab
from matplotlib.patches import Rectangle

class Options(object):
    """Class to provide matplotlib options handling in Ekin"""

    colors = ['b','g','r','y','m','c','k',
              '#0049B4','#C90B11','#437C17','#AFC7C7','#E9AB17','#7F525D',
              '#F6358A','#52D017','#FFFC17','#F76541','#F62217' ]
    linestyles = ['-','--']
    shapes = ['o','^','v','>','<','s','+','x','p','d','h','*','-','--',':','.',':.',',','|'] 
    legend_positions = ['best', 'upper left','upper center','upper right',
                         'center left','center','center right'
                         'lower left','lower center','lower right']

    graphtypes = ['XY', 'bar']
    fonts = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']

    def __init__(self, redraw=None, opts={}):
        """Setup variables"""      
        self.redraw = redraw       
        self.datacolors = self.colors
        self.dpi = 300
        self.opts = {'shape':'o', 'markersize':20, 'grid':0,
                     'xscale':0, 'yscale':0, 'showlegend':0,
                     'legendloc':'best', 'graphtype':'XY',
                     'linewidth':1.0, 'font':'monospace', 'fontsize':12,
                     'normalise':False, 'alpha':0.7, 'showerrorbars':False,
                     'usetex':False, 'title':'', 'xlabel':'','ylabel':'',
                     'grayscale':False}        
        self.setOptions(**opts)        
        self.currdata = None
        self.format = None  #data format   
        self.setupPlotVars()        
        return

    def setData(self, data):
        """Set the current plot data, useful for re-plotting without re-calling
           explicit functions from the parent"""
        self.currdata = data
        return

    def hasData(self):
        """Is there some plot data?"""
        if self.currdata != None and len(self.currdata) > 0:
            return True
        else:
            return False

    def setDataSeries(self, names=None, start=1):
        """Set the series names, for use in legend"""
        self.dataseriesvars=[]
        for i in range(start,len(names)):
           s=StringVar()
           s.set(names[i])
           self.dataseriesvars.append(s)
        
        return

    def setFormat(self, format):
        """Set current data format of currdata"""
        self.format = format
        return

    def setTitle(self, title=None):
        self.title = title

    def setxlabel(self, label=None):
        self.xlabel = label

    def setylabel(self, label=None):
        self.ylabel = label

    def setOptions(self, **kwargs):
        """Set the options before plotting"""
        for key in kwargs:    
            self.opts[key] = kwargs[key]        
        for key in self.opts:
            self.__dict__[key] = self.opts[key]
        pylab.rc("font", family=self.font, size=self.fontsize)
        return

    def setupPlotVars(self):
        """Plot Vars """
        self.pltgrid = IntVar()
        self.pltgrid.set(self.grid)
        self.pltlegend = IntVar()
        self.pltsymbol = StringVar()
        print self.shape
        self.pltsymbol.set(self.shape)
        self.markersizevar = IntVar()
        self.markersizevar.set(self.markersize)
        self.legendlocvar = StringVar()
        self.legendlocvar.set(self.legendloc)
        self.xscalevar = IntVar()
        self.yscalevar = IntVar()
        self.xscalevar.set(0)
        self.yscalevar.set(0)
        self.showerrorbarsvar = IntVar()
        self.showerrorbarsvar.set(self.showerrorbars)
        self.graphtypevar = StringVar()
        self.graphtypevar.set(self.graphtype)
        self.linewidthvar = DoubleVar()
        self.linewidthvar.set(self.linewidth)
        self.fontvar = StringVar()
        self.fontvar.set(self.font)
        self.fontsizevar = DoubleVar()
        self.fontsizevar.set(self.fontsize)
        self.normalisevar = IntVar()
        self.normalisevar.set(0)
        self.alphavar = DoubleVar()
        self.alphavar.set(self.alpha)
        self.usetexvar = IntVar()
        self.usetexvar.set(self.usetex)
        #plot specific
        self.plottitlevar = StringVar()
        self.plottitlevar.set(self.title)
        self.plotxlabelvar = StringVar()
        self.plotxlabelvar.set(self.xlabel)
        self.plotylabelvar = StringVar()
        self.plotylabelvar.set(self.ylabel)
        self.varyshapesvar = IntVar()
        self.varyshapesvar.set(0)
        self.grayscalevar = IntVar()
        self.grayscalevar.set(0)        
        self.dataseriesvars=[]
        return


    def applyOptions(self):
        """Apply the gui option vars to the plotter options"""
        self.setOptions(shape=self.pltsymbol.get(), grid=self.pltgrid.get(),
               xscale=self.xscalevar.get(), yscale=self.yscalevar.get(),
               showlegend = self.pltlegend.get(),
               legendloc = self.legendlocvar.get(),
               linewidth = self.linewidthvar.get(),
               graphtype = self.graphtypevar.get(),
               font = self.fontvar.get(),
               fontsize = self.fontsizevar.get(),
               title = self.plottitlevar.get())
        self.setTitle(self.plottitlevar.get())
        self.setxlabel(self.plotxlabelvar.get())
        self.setylabel(self.plotylabelvar.get())
        self.opts={}
        self.opts = {'marker':self.pltsymbol.get(),
                'markersize':self.markersizevar.get(),
                'title':self.plottitlevar.get(),
                'font':self.fontvar.get(),
                'fontsize':self.fontsizevar.get(),
                'linewidth':self.linewidthvar.get(),
                'legend':self.pltlegend.get(),
                'legendloc':self.legendlocvar.get(),
                'title':self.plottitlevar.get(),
                'xlabel':self.plotxlabelvar.get(),
                'ylabel':self.plotylabelvar.get(),
                'logx':self.xscalevar.get(),
                'logy':self.yscalevar.get(),
                'grid':self.pltgrid.get(),
                'graphtype':self.graphtypevar.get(),
                'normalise':self.normalisevar.get(),
                'alpha':self.alphavar.get(),
                'usetex':self.usetexvar.get(),     
                'showerrorbars':self.showerrorbarsvar.get(),
                'varyshapes':self.varyshapesvar.get(),
                'grayscale':self.grayscalevar.get()}
        if self.redraw != None:
            self.redraw(options=self.opts)            
        return

    def plotSetup(self, data=None):
        """Plot options dialog"""
        
        if data != None:
            self.setData(data)
        self.plotprefswin=Toplevel()
        self.plotprefswin.geometry('+300+450')
        self.plotprefswin.title('Plot Preferences')
        row=0
        frame1=LabelFrame(self.plotprefswin, text='General')
        frame1.grid(row=0,column=0,sticky='news',padx=2,pady=2)
        def close_prefsdialog():
            self.plotprefswin.destroy()

        def choosecolor(x):
            """Choose color for data series"""
            d=x[0]
            c=x[1]
            print 'passed', 'd',d, 'c',c
            import tkColorChooser
            colour,colour_string = tkColorChooser.askcolor(c,parent=self.plotprefswin)
            if colour != None:
                self.datacolors[d] = str(colour_string)
                cbuttons[d].configure(bg=colour_string)
            return

        Checkbutton(frame1, text="Grid lines", variable=self.pltgrid,
                    onvalue=1, offvalue=0).grid(row=0,column=0, columnspan=2, sticky='news')
        Checkbutton(frame1, text="Legend", variable=self.pltlegend,
                    onvalue=1, offvalue=0).grid(row=1,column=0, columnspan=2, sticky='news')
        Checkbutton(frame1, text="Normalise", variable=self.normalisevar,
                    onvalue=1, offvalue=0).grid(row=2,column=0, columnspan=2, sticky='news')                    
        Checkbutton(frame1, text="Show error bars", variable=self.showerrorbarsvar,
                    onvalue=1, offvalue=0).grid(row=3,column=0, columnspan=2, sticky='news')

        Label(frame1,text='Symbol:').grid(row=4,column=0,padx=2,pady=2)
        symbolbutton = Menubutton(frame1,textvariable=self.pltsymbol,
					                relief=GROOVE, width=16, bg='lightblue')
        symbol_menu = Menu(symbolbutton, tearoff=0)
        symbolbutton['menu'] = symbol_menu
        for text in self.shapes:
            symbol_menu.add_radiobutton(label=text,
                                            variable=self.pltsymbol,
                                            value=text,
                                            indicatoron=1)
        symbolbutton.grid(row=4,column=1, sticky='news',padx=2,pady=2)
        row=row+1
        Label(frame1,text='Legend pos:').grid(row=5,column=0,padx=2,pady=2)
        legendposbutton = Menubutton(frame1,textvariable=self.legendlocvar,
					                relief=GROOVE, width=16, bg='lightblue')
        legendpos_menu = Menu(legendposbutton, tearoff=0)
        legendposbutton['menu'] = legendpos_menu
        i=0
        for p in self.legend_positions:
            legendpos_menu.add_radiobutton(label=p,
                                        variable=self.legendlocvar,
                                        value=p,
                                        indicatoron=1)
            i+=1
        legendposbutton.grid(row=5,column=1, sticky='news',padx=2,pady=2)
        Checkbutton(frame1, text="Use latex", variable=self.usetexvar,
                    onvalue=1, offvalue=0).grid(row=6,column=0, columnspan=2, sticky='news')
            
        frame2=LabelFrame(self.plotprefswin, text='Format')
        frame2.grid(row=0,column=1,rowspan=2,sticky='news',padx=2,pady=2)

        Label(frame2,text='Font:').grid(row=0,column=0,padx=2,pady=2)
        fontbutton = Menubutton(frame2,textvariable=self.fontvar,
					                relief=GROOVE, width=16, bg='lightblue')
        font_menu = Menu(fontbutton, tearoff=0)
        fontbutton['menu'] = font_menu
        for f in self.fonts:
            font_menu.add_radiobutton(label=f,
                                            variable=self.fontvar,
                                            value=f,
                                            indicatoron=1)
        fontbutton.grid(row=0,column=1, sticky='news',padx=2,pady=2)
        row=row+1
        Label(frame2,text='Font size:').grid(row=1,column=0,padx=2,pady=2)
        Scale(frame2,from_=8,to=26,resolution=0.5,orient='horizontal',
                            relief=GROOVE,variable=self.fontsizevar).grid(row=1,column=1,padx=2,pady=2)


        Label(frame2,text='marker size:').grid(row=2,column=0,padx=2,pady=2)
        Scale(frame2,from_=10,to=200,resolution=5,orient='horizontal',
                            relief=GROOVE,variable=self.markersizevar).grid(row=2,column=1,padx=2,pady=2)

        Label(frame2,text='linewidth:').grid(row=3,column=0,padx=2,pady=2)
        Scale(frame2,from_=0,to=10,resolution=0.5,orient='horizontal',
                            relief=GROOVE,variable=self.linewidthvar).grid(row=3,column=1,padx=2,pady=2)

        Label(frame2,text='transparency:').grid(row=4,column=0,padx=2,pady=2)
        Scale(frame2,from_=0.1,to=1,resolution=0.1,orient='horizontal',
                            relief=GROOVE,variable=self.alphavar).grid(row=4,column=1,padx=2,pady=2)

        Checkbutton(frame2, text="vary shapes", variable=self.varyshapesvar,
                    onvalue=1, offvalue=0).grid(row=5,column=0,columnspan=2,sticky='news')
        Checkbutton(frame2, text="grayscale", variable=self.grayscalevar,
                    onvalue=1, offvalue=0).grid(row=6,column=0,columnspan=2,sticky='news')                    
                    
        scalesframe = LabelFrame(self.plotprefswin, text="Axes Scales")
        scales={0:'norm',1:'log'}
        for i in range(0,2):
            Radiobutton(scalesframe,text='x-'+scales[i],variable=self.xscalevar,
                            value=i).grid(row=0,column=i,pady=2)
            Radiobutton(scalesframe,text='y-'+scales[i],variable=self.yscalevar,
                            value=i).grid(row=1,column=i,pady=2)
        scalesframe.grid(row=1,column=0,sticky='news',padx=2,pady=2)

        row=row+1
        frame=LabelFrame(self.plotprefswin, text='Graph type')
        frame.grid(row=row,column=0,columnspan=2,sticky='news',padx=2,pady=2)
        for i in range(len(self.graphtypes)):
            Radiobutton(frame,text=self.graphtypes[i],variable=self.graphtypevar,
                            value=self.graphtypes[i]).grid(row=0,column=i,pady=2)

        row=row+1
        labelsframe = LabelFrame(self.plotprefswin,text='Labels')
        labelsframe.grid(row=row,column=0,columnspan=2,sticky='news',padx=2,pady=2)
        Label(labelsframe,text='Title:').grid(row=0,column=0,padx=2,pady=2)
        Entry(labelsframe,textvariable=self.plottitlevar,bg='white',relief=GROOVE).grid(row=0,column=1,padx=2,pady=2)
        Label(labelsframe,text='X-axis label:').grid(row=1,column=0,padx=2,pady=2)
        Entry(labelsframe,textvariable=self.plotxlabelvar,bg='white',relief=GROOVE).grid(row=1,column=1,padx=2,pady=2)
        Label(labelsframe,text='Y-axis label:').grid(row=2,column=0,padx=2,pady=2)
        Entry(labelsframe,textvariable=self.plotylabelvar,bg='white',relief=GROOVE).grid(row=2,column=1,padx=2,pady=2)
        #print self.currdata
        if self.currdata != None:       
            row=row+1
            seriesframe = LabelFrame(self.plotprefswin, text="Data Series Labels")
            seriesframe.grid(row=row,column=0,columnspan=2,sticky='news',padx=2,pady=2)
           
            if len(self.dataseriesvars) == 0:
                self.setDataSeries(range(len(self.currdata)))
            r=1
            sr=1
            cl=0
            for s in self.dataseriesvars:
                Label(seriesframe,text='Series '+str(r)).grid(row=r,column=cl,padx=2,pady=2)
                Entry(seriesframe,textvariable=s,bg='white',
                                          relief=GROOVE).grid(row=r,column=cl+1,padx=2,pady=2)
                r+=1
                if r > 8:
                    r=1
                    cl+=2
            row=row+1
            cbuttons = {}
            frame = LabelFrame(self.plotprefswin, text="Dataset Colors")
            r=1
            cl=0
            sr=1
            ci=0
            for d in range(len(self.dataseriesvars)):
                if d >= len(self.datacolors):
                    self.datacolors.append(self.colors[ci])
                    ci+=1
                c = self.datacolors[d]
                action = lambda x =(d,c): choosecolor(x)
                cbuttons[d]=Button(frame,text='Series '+str(sr),bg=c,command=action)
                cbuttons[d].grid(row=r,column=cl,sticky='news',padx=2,pady=2)
                r+=1
                sr+=1
                if r > 8:
                    r=1
                    cl+=1
            frame.grid(row=row,column=0,columnspan=2,sticky='news',padx=2,pady=2)

        row=row+1
        frame=Frame(self.plotprefswin)
        frame.grid(row=row,column=0,columnspan=2,sticky='news',padx=2,pady=2)        
        b = Button(frame, text="Apply", command=self.applyOptions, relief=GROOVE, bg='#99ccff')
        b.pack(side=LEFT,fill=X,padx=2,pady=2)
        c=Button(frame,text='Close', command=close_prefsdialog, relief=GROOVE, bg='#99ccff')
        c.pack(side=LEFT,fill=X,padx=2,pady=2)        
        self.plotprefswin.focus_set()
        self.plotprefswin.grab_set()
        return


class PylabHelper():
    """Utilities for pylab ekin plotting"""
    def __init__(self):

        return

    def setInactivePoints(cls):
        """Set points that are inactive to a different color"""
        return

class MouseMonitor:
    """Class to handle mouse click actions on plots"""
    event = None

    def __init__(self, ax, parent):
        self.ax = ax
        self.parent = parent
        self.press = False
        self.rect = None
        return

    def connect(self):
        self.cidpress = self.ax.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.ax.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.ax.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        """Handle mouse click"""
        self.press = True
        self.parent.selection = None
        if self.rect != None:
            self.rect.set_visible(False)
            self.ax.patches = []
            self.ax.figure.canvas.draw()
            self.rect=None
        self.x = event.xdata; self.y = event.ydata
        return

    def on_motion(self, event):
        """Draw a selection rect"""
        if self.press == False:
            return
        x = event.xdata; y = event.ydata
        if x == None or y==None:
            return
            '''print self.prevx, self.x
            xmin, xmax = self.ax.get_xlim()
            ymin, ymax = self.ax.get_ylim()
            if self.prevx<self.x:
                x=xmin
            elif self.prevx>self.x:
                x=xmax
            if self.prevy<self.y:
                y=ymin
            elif self.prevy>self.y:
                y=ymax'''
        
        dx = x-self.x; dy=y-self.y
        if self.rect == None:
            #print 'new'
            self.rect = Rectangle((self.x,self.y),dx,dy, fc='lightblue',ec='blue',alpha=0.6)
            self.ax.add_patch(self.rect)
        else:
            self.rect.set_width(dx)
            self.rect.set_height(dy)

        #draw selection rect
        self.ax.figure.canvas.draw()
        self.parent.selection = (self.x, self.y, x, y)
        if x!=None: self.prevx=x
        if y!=None: self.prevy=y
        return

    def on_release(self, event):
        self.press = False
        return

    def disconnect(self):
        """Disconnect all the stored connection ids"""
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)

