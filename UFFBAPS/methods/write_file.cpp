/*
 #
 # UFFBAPS - Unified Force Field for Binding And Protein Stability
 # Copyright (C) 2010 Jens Erik Nielsen & Chresten Soendergaard
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
 */


#include "write_file.h"


Write_File::Write_File():Method(){}

Write_File::Write_File(FILE * reporter):Method(reporter)
{
  /*** write out to out file **/
  writeDescription(reporter);
  
}

Write_File::Write_File(FILE * reporter, vector<Soup*> A, string format):Method(reporter)
{
  /*** write out to out file **/
  writeDescription(reporter);
  vector<string> remarks;
  write(A, format, remarks, "out.pdb");
}

Write_File::~Write_File(){}

void Write_File::write(vector<Soup*> A, string format, vector<string> remarks, string filename)
{

  atom_serial = 0;
  residue_serial = 0;

  /*** open out file ***/
  out = fopen(filename.c_str(), "w");
 

  fprintf(out,"Generated by bla bla\n");
 
  /*** print remarks ***/
  for(vector<string>::iterator l = remarks.begin(); l!=remarks.end(); l++)
    fprintf(out,"REMARK:%s\n",(*l).c_str());

  /*** print atoms ***/
  for(vector<Soup*>::iterator soup = A.begin(); soup != A.end(); soup++)
    {
      vector<vector<SoupObject*> > objects = (*soup)->getSoupObjects();
      
      /*** write protein chains ***/
      write_objects(objects[0], format, "ATOM  ");

      /*** write molecules ***/
      write_objects(objects[1], format, "HETATM");

      /*** write waters ***/
      write_objects(objects[2], format, "HETATM");


    }
  fprintf(out,"END\n"); 

  fclose(out);
}




void Write_File::write_objects(vector<SoupObject*> objects, string format, string prefix)
{
  for(vector<SoupObject*>::iterator object = objects.begin(); object != objects.end(); object++)
    {
      vector<Atom*> atoms = (*object)->getAtoms();
     
      write_atoms(atoms, format, prefix);
    }

}

void Write_File::write_atoms(vector<Atom*> atoms, string format, string prefix, string filename)
{
  atom_serial = 0;
  residue_serial = 0;

  /*** open out file ***/
  out = fopen(filename.c_str(), "w");

  write_atoms(atoms, format, prefix);

 
  fprintf(out,"END\n"); 
  fclose(out);


}


void Write_File::write_atoms(vector<Atom*> atoms, string format, string prefix)
{
  int this_residue = -10000;

  for(vector<Atom*>::iterator atom = atoms.begin(); atom != atoms.end(); atom++)
    {
      
      /*** update serials ***/
      atom_serial++;
      if (this_residue != (*atom)->residue_no)
	{
	  residue_serial++;
	  this_residue = (*atom)->residue_no;
	}
      
      
      /*** format atom name ***/
      string name = (*atom)->name;
      string formatted_name;
      switch(name.size())
	{	
	case 1:
	  formatted_name = " "+name+"  ";
	  break;
	case 2:
	  formatted_name = " "+name+" ";
	  break;
	case 3:
	  formatted_name = " "+name;
	  break;
	case 4:
	  formatted_name = name;
	  break;
	}
      
      /*** write line in pdb format ***/
      if (format == "pdb")
	fprintf(out,"%6s%5d %4s %3s   %3d    %8.3f%8.3f%8.3f%6.2f%6.2f          %2s\n",
		prefix.c_str(),
		atom_serial, formatted_name.c_str(),
		(*atom)->residue.c_str(), residue_serial,
		(*atom)->x,(*atom)->y,(*atom)->z,
		(*atom)->occupancy,(*atom)->tempFactor, (*atom)->element.c_str());
      /*** write line in pqr format ***/
      else if (format == "pqr")
	fprintf(out,"%6s%5d  %4s %3s  %3d    %8.3f%8.3f%8.3f%6.2f%6.2f          %2s\n",
		prefix.c_str(),
		atom_serial, formatted_name.c_str(),
		(*atom)->residue.c_str(), residue_serial,
		(*atom)->x,(*atom)->y,(*atom)->z,
		(*atom)->charge, (*atom)->vdw_dist, (*atom)->element.c_str());
      
    }
  fprintf(out,"TER\n");
  
  return;

}



void Write_File::writeDescription(FILE * reporter)
{
  /*** write out to out file **/
  version =string("$Id: write_file.cpp 6326 2010-08-26 16:08:21Z nielsen $");

  description = 
     string("");

  fprintf(reporter,"%s\n",version.c_str());	
  fprintf(reporter,"%s\n",description.c_str());
}