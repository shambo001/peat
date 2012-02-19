from distutils.core import setup
import sys,os
home=os.path.expanduser('~')
pythonpath=os.path.join(home,'python')

setup(name='PEATDB', version='2.0',
	description='Protein Engineering Analysis Tool',
	author='Nielsen Group, UCD',
	author_email='PEAT_support@ucd.ie',
	url='http://enzyme.ucd.ie/PEAT',
	license='For academic and non-profit use only. No redistribution, no alterations.',
	packages=['PEATDB','PEATDB.DNAtool','PEATDB.Ekin',
		  'Protool','pKaTool','DataPipeline'],
	package_dir={'':pythonpath},
	package_data={'DNAtool':['restriction_enzymes.DAT','DNAtool.ico'], 
		      'PEAT_DB':['logo.gif','App.ico','data/AA_masses.txt'],
		      'Protool':['AA.DAT','bbdep02.May.sortlib']},
	requires=['Pmw','numpy'],
)
