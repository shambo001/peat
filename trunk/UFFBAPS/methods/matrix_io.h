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

#ifndef MATRIX_IO_H
#define MATRIX_IO_H
#include "method.h"

#include <boost/numeric/ublas/matrix.hpp>

using namespace std;
namespace la = boost::numeric::ublas;

class Matrix_IO:  Method{

 public:
  Matrix_IO(FILE * reporter);
  Matrix_IO();
  ~Matrix_IO();

  int open(string filename);
  void write_matrix(string name, la::matrix<double> m);
  void write_vector(string name, la::vector<double> v);
  void write_matrix(string name, vector<vector<double> > m);
  void write_vector(string name, vector<double> v);
  void write_string_vector(string name, vector<string> v);
  void update_lists(vector<string> names, la::matrix<double> to_a, la::vector<double> to_b);
  void close();

 private:
  FILE * out;
  FILE * lista;
  FILE * listb;
  void writeDescription(FILE * reporter);
};

#endif
