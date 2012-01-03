# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_FFFcontrol', [dirname(__file__)])
        except ImportError:
            import _FFFcontrol
            return _FFFcontrol
        if fp is not None:
            try:
                _mod = imp.load_module('_FFFcontrol', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _FFFcontrol = swig_import_helper()
    del swig_import_helper
else:
    import _FFFcontrol
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _FFFcontrol.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _FFFcontrol.SwigPyIterator_value(self)
    def incr(self, n = 1): return _FFFcontrol.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _FFFcontrol.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _FFFcontrol.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _FFFcontrol.SwigPyIterator_equal(self, *args)
    def copy(self): return _FFFcontrol.SwigPyIterator_copy(self)
    def next(self): return _FFFcontrol.SwigPyIterator_next(self)
    def __next__(self): return _FFFcontrol.SwigPyIterator___next__(self)
    def previous(self): return _FFFcontrol.SwigPyIterator_previous(self)
    def advance(self, *args): return _FFFcontrol.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _FFFcontrol.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _FFFcontrol.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _FFFcontrol.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _FFFcontrol.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _FFFcontrol.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _FFFcontrol.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _FFFcontrol.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _FFFcontrol.IntVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _FFFcontrol.IntVector___nonzero__(self)
    def __bool__(self): return _FFFcontrol.IntVector___bool__(self)
    def __len__(self): return _FFFcontrol.IntVector___len__(self)
    def pop(self): return _FFFcontrol.IntVector_pop(self)
    def __getslice__(self, *args): return _FFFcontrol.IntVector___getslice__(self, *args)
    def __setslice__(self, *args): return _FFFcontrol.IntVector___setslice__(self, *args)
    def __delslice__(self, *args): return _FFFcontrol.IntVector___delslice__(self, *args)
    def __delitem__(self, *args): return _FFFcontrol.IntVector___delitem__(self, *args)
    def __getitem__(self, *args): return _FFFcontrol.IntVector___getitem__(self, *args)
    def __setitem__(self, *args): return _FFFcontrol.IntVector___setitem__(self, *args)
    def append(self, *args): return _FFFcontrol.IntVector_append(self, *args)
    def empty(self): return _FFFcontrol.IntVector_empty(self)
    def size(self): return _FFFcontrol.IntVector_size(self)
    def clear(self): return _FFFcontrol.IntVector_clear(self)
    def swap(self, *args): return _FFFcontrol.IntVector_swap(self, *args)
    def get_allocator(self): return _FFFcontrol.IntVector_get_allocator(self)
    def begin(self): return _FFFcontrol.IntVector_begin(self)
    def end(self): return _FFFcontrol.IntVector_end(self)
    def rbegin(self): return _FFFcontrol.IntVector_rbegin(self)
    def rend(self): return _FFFcontrol.IntVector_rend(self)
    def pop_back(self): return _FFFcontrol.IntVector_pop_back(self)
    def erase(self, *args): return _FFFcontrol.IntVector_erase(self, *args)
    def __init__(self, *args): 
        this = _FFFcontrol.new_IntVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _FFFcontrol.IntVector_push_back(self, *args)
    def front(self): return _FFFcontrol.IntVector_front(self)
    def back(self): return _FFFcontrol.IntVector_back(self)
    def assign(self, *args): return _FFFcontrol.IntVector_assign(self, *args)
    def resize(self, *args): return _FFFcontrol.IntVector_resize(self, *args)
    def insert(self, *args): return _FFFcontrol.IntVector_insert(self, *args)
    def reserve(self, *args): return _FFFcontrol.IntVector_reserve(self, *args)
    def capacity(self): return _FFFcontrol.IntVector_capacity(self)
    __swig_destroy__ = _FFFcontrol.delete_IntVector
    __del__ = lambda self : None;
IntVector_swigregister = _FFFcontrol.IntVector_swigregister
IntVector_swigregister(IntVector)

class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _FFFcontrol.DoubleVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _FFFcontrol.DoubleVector___nonzero__(self)
    def __bool__(self): return _FFFcontrol.DoubleVector___bool__(self)
    def __len__(self): return _FFFcontrol.DoubleVector___len__(self)
    def pop(self): return _FFFcontrol.DoubleVector_pop(self)
    def __getslice__(self, *args): return _FFFcontrol.DoubleVector___getslice__(self, *args)
    def __setslice__(self, *args): return _FFFcontrol.DoubleVector___setslice__(self, *args)
    def __delslice__(self, *args): return _FFFcontrol.DoubleVector___delslice__(self, *args)
    def __delitem__(self, *args): return _FFFcontrol.DoubleVector___delitem__(self, *args)
    def __getitem__(self, *args): return _FFFcontrol.DoubleVector___getitem__(self, *args)
    def __setitem__(self, *args): return _FFFcontrol.DoubleVector___setitem__(self, *args)
    def append(self, *args): return _FFFcontrol.DoubleVector_append(self, *args)
    def empty(self): return _FFFcontrol.DoubleVector_empty(self)
    def size(self): return _FFFcontrol.DoubleVector_size(self)
    def clear(self): return _FFFcontrol.DoubleVector_clear(self)
    def swap(self, *args): return _FFFcontrol.DoubleVector_swap(self, *args)
    def get_allocator(self): return _FFFcontrol.DoubleVector_get_allocator(self)
    def begin(self): return _FFFcontrol.DoubleVector_begin(self)
    def end(self): return _FFFcontrol.DoubleVector_end(self)
    def rbegin(self): return _FFFcontrol.DoubleVector_rbegin(self)
    def rend(self): return _FFFcontrol.DoubleVector_rend(self)
    def pop_back(self): return _FFFcontrol.DoubleVector_pop_back(self)
    def erase(self, *args): return _FFFcontrol.DoubleVector_erase(self, *args)
    def __init__(self, *args): 
        this = _FFFcontrol.new_DoubleVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _FFFcontrol.DoubleVector_push_back(self, *args)
    def front(self): return _FFFcontrol.DoubleVector_front(self)
    def back(self): return _FFFcontrol.DoubleVector_back(self)
    def assign(self, *args): return _FFFcontrol.DoubleVector_assign(self, *args)
    def resize(self, *args): return _FFFcontrol.DoubleVector_resize(self, *args)
    def insert(self, *args): return _FFFcontrol.DoubleVector_insert(self, *args)
    def reserve(self, *args): return _FFFcontrol.DoubleVector_reserve(self, *args)
    def capacity(self): return _FFFcontrol.DoubleVector_capacity(self)
    __swig_destroy__ = _FFFcontrol.delete_DoubleVector
    __del__ = lambda self : None;
DoubleVector_swigregister = _FFFcontrol.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)

class FloatVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FloatVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FloatVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _FFFcontrol.FloatVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _FFFcontrol.FloatVector___nonzero__(self)
    def __bool__(self): return _FFFcontrol.FloatVector___bool__(self)
    def __len__(self): return _FFFcontrol.FloatVector___len__(self)
    def pop(self): return _FFFcontrol.FloatVector_pop(self)
    def __getslice__(self, *args): return _FFFcontrol.FloatVector___getslice__(self, *args)
    def __setslice__(self, *args): return _FFFcontrol.FloatVector___setslice__(self, *args)
    def __delslice__(self, *args): return _FFFcontrol.FloatVector___delslice__(self, *args)
    def __delitem__(self, *args): return _FFFcontrol.FloatVector___delitem__(self, *args)
    def __getitem__(self, *args): return _FFFcontrol.FloatVector___getitem__(self, *args)
    def __setitem__(self, *args): return _FFFcontrol.FloatVector___setitem__(self, *args)
    def append(self, *args): return _FFFcontrol.FloatVector_append(self, *args)
    def empty(self): return _FFFcontrol.FloatVector_empty(self)
    def size(self): return _FFFcontrol.FloatVector_size(self)
    def clear(self): return _FFFcontrol.FloatVector_clear(self)
    def swap(self, *args): return _FFFcontrol.FloatVector_swap(self, *args)
    def get_allocator(self): return _FFFcontrol.FloatVector_get_allocator(self)
    def begin(self): return _FFFcontrol.FloatVector_begin(self)
    def end(self): return _FFFcontrol.FloatVector_end(self)
    def rbegin(self): return _FFFcontrol.FloatVector_rbegin(self)
    def rend(self): return _FFFcontrol.FloatVector_rend(self)
    def pop_back(self): return _FFFcontrol.FloatVector_pop_back(self)
    def erase(self, *args): return _FFFcontrol.FloatVector_erase(self, *args)
    def __init__(self, *args): 
        this = _FFFcontrol.new_FloatVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _FFFcontrol.FloatVector_push_back(self, *args)
    def front(self): return _FFFcontrol.FloatVector_front(self)
    def back(self): return _FFFcontrol.FloatVector_back(self)
    def assign(self, *args): return _FFFcontrol.FloatVector_assign(self, *args)
    def resize(self, *args): return _FFFcontrol.FloatVector_resize(self, *args)
    def insert(self, *args): return _FFFcontrol.FloatVector_insert(self, *args)
    def reserve(self, *args): return _FFFcontrol.FloatVector_reserve(self, *args)
    def capacity(self): return _FFFcontrol.FloatVector_capacity(self)
    __swig_destroy__ = _FFFcontrol.delete_FloatVector
    __del__ = lambda self : None;
FloatVector_swigregister = _FFFcontrol.FloatVector_swigregister
FloatVector_swigregister(FloatVector)

class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _FFFcontrol.StringVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _FFFcontrol.StringVector___nonzero__(self)
    def __bool__(self): return _FFFcontrol.StringVector___bool__(self)
    def __len__(self): return _FFFcontrol.StringVector___len__(self)
    def pop(self): return _FFFcontrol.StringVector_pop(self)
    def __getslice__(self, *args): return _FFFcontrol.StringVector___getslice__(self, *args)
    def __setslice__(self, *args): return _FFFcontrol.StringVector___setslice__(self, *args)
    def __delslice__(self, *args): return _FFFcontrol.StringVector___delslice__(self, *args)
    def __delitem__(self, *args): return _FFFcontrol.StringVector___delitem__(self, *args)
    def __getitem__(self, *args): return _FFFcontrol.StringVector___getitem__(self, *args)
    def __setitem__(self, *args): return _FFFcontrol.StringVector___setitem__(self, *args)
    def append(self, *args): return _FFFcontrol.StringVector_append(self, *args)
    def empty(self): return _FFFcontrol.StringVector_empty(self)
    def size(self): return _FFFcontrol.StringVector_size(self)
    def clear(self): return _FFFcontrol.StringVector_clear(self)
    def swap(self, *args): return _FFFcontrol.StringVector_swap(self, *args)
    def get_allocator(self): return _FFFcontrol.StringVector_get_allocator(self)
    def begin(self): return _FFFcontrol.StringVector_begin(self)
    def end(self): return _FFFcontrol.StringVector_end(self)
    def rbegin(self): return _FFFcontrol.StringVector_rbegin(self)
    def rend(self): return _FFFcontrol.StringVector_rend(self)
    def pop_back(self): return _FFFcontrol.StringVector_pop_back(self)
    def erase(self, *args): return _FFFcontrol.StringVector_erase(self, *args)
    def __init__(self, *args): 
        this = _FFFcontrol.new_StringVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _FFFcontrol.StringVector_push_back(self, *args)
    def front(self): return _FFFcontrol.StringVector_front(self)
    def back(self): return _FFFcontrol.StringVector_back(self)
    def assign(self, *args): return _FFFcontrol.StringVector_assign(self, *args)
    def resize(self, *args): return _FFFcontrol.StringVector_resize(self, *args)
    def insert(self, *args): return _FFFcontrol.StringVector_insert(self, *args)
    def reserve(self, *args): return _FFFcontrol.StringVector_reserve(self, *args)
    def capacity(self): return _FFFcontrol.StringVector_capacity(self)
    __swig_destroy__ = _FFFcontrol.delete_StringVector
    __del__ = lambda self : None;
StringVector_swigregister = _FFFcontrol.StringVector_swigregister
StringVector_swigregister(StringVector)

class Control(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Control, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Control, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _FFFcontrol.new_Control(*args)
        try: self.this.append(this)
        except: self.this = this
    def interpreter(self): return _FFFcontrol.Control_interpreter(self)
    def run_command(self, *args): return _FFFcontrol.Control_run_command(self, *args)
    __swig_setmethods__["Proteins"] = _FFFcontrol.Control_Proteins_set
    __swig_getmethods__["Proteins"] = _FFFcontrol.Control_Proteins_get
    if _newclass:Proteins = _swig_property(_FFFcontrol.Control_Proteins_get, _FFFcontrol.Control_Proteins_set)
    __swig_setmethods__["Protein_names"] = _FFFcontrol.Control_Protein_names_set
    __swig_getmethods__["Protein_names"] = _FFFcontrol.Control_Protein_names_get
    if _newclass:Protein_names = _swig_property(_FFFcontrol.Control_Protein_names_get, _FFFcontrol.Control_Protein_names_set)
    __swig_setmethods__["Model_instance"] = _FFFcontrol.Control_Model_instance_set
    __swig_getmethods__["Model_instance"] = _FFFcontrol.Control_Model_instance_get
    if _newclass:Model_instance = _swig_property(_FFFcontrol.Control_Model_instance_get, _FFFcontrol.Control_Model_instance_set)
    __swig_setmethods__["running"] = _FFFcontrol.Control_running_set
    __swig_getmethods__["running"] = _FFFcontrol.Control_running_get
    if _newclass:running = _swig_property(_FFFcontrol.Control_running_get, _FFFcontrol.Control_running_set)
    __swig_destroy__ = _FFFcontrol.delete_Control
    __del__ = lambda self : None;
Control_swigregister = _FFFcontrol.Control_swigregister
Control_swigregister(Control)

class FFF(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FFF, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FFF, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _FFFcontrol.new_FFF()
        try: self.this.append(this)
        except: self.this = this
    def read_pdb(self, *args): return _FFFcontrol.FFF_read_pdb(self, *args)
    def write_pdb(self, *args): return _FFFcontrol.FFF_write_pdb(self, *args)
    def writepdb(self, *args): return _FFFcontrol.FFF_writepdb(self, *args)
    def write_pqr(self, *args): return _FFFcontrol.FFF_write_pqr(self, *args)
    def make_pdblines(self, *args): return _FFFcontrol.FFF_make_pdblines(self, *args)
    def make_pdbline(self, *args): return _FFFcontrol.FFF_make_pdbline(self, *args)
    def parse_lines(self, *args): return _FFFcontrol.FFF_parse_lines(self, *args)
    def remove_atoms_with_tag(self, *args): return _FFFcontrol.FFF_remove_atoms_with_tag(self, *args)
    def remove_atom(self, *args): return _FFFcontrol.FFF_remove_atom(self, *args)
    def soup_stat(self): return _FFFcontrol.FFF_soup_stat(self)
    def check_soup(self): return _FFFcontrol.FFF_check_soup(self)
    def update_all_atoms(self): return _FFFcontrol.FFF_update_all_atoms(self)
    def update_BOXLJ(self): return _FFFcontrol.FFF_update_BOXLJ(self)
    def update_BOX10A(self): return _FFFcontrol.FFF_update_BOX10A(self)
    def set_pH(self, *args): return _FFFcontrol.FFF_set_pH(self, *args)
    def are_bonded(self, *args): return _FFFcontrol.FFF_are_bonded(self, *args)
    def are_1_3_bonded(self, *args): return _FFFcontrol.FFF_are_1_3_bonded(self, *args)
    def are_1_4_bonded(self, *args): return _FFFcontrol.FFF_are_1_4_bonded(self, *args)
    def could_be_Hbonded(self, *args): return _FFFcontrol.FFF_could_be_Hbonded(self, *args)
    def find_residue(self, *args): return _FFFcontrol.FFF_find_residue(self, *args)
    __swig_setmethods__["chains"] = _FFFcontrol.FFF_chains_set
    __swig_getmethods__["chains"] = _FFFcontrol.FFF_chains_get
    if _newclass:chains = _swig_property(_FFFcontrol.FFF_chains_get, _FFFcontrol.FFF_chains_set)
    __swig_setmethods__["amino_acids"] = _FFFcontrol.FFF_amino_acids_set
    __swig_getmethods__["amino_acids"] = _FFFcontrol.FFF_amino_acids_get
    if _newclass:amino_acids = _swig_property(_FFFcontrol.FFF_amino_acids_get, _FFFcontrol.FFF_amino_acids_set)
    __swig_setmethods__["pdbname"] = _FFFcontrol.FFF_pdbname_set
    __swig_getmethods__["pdbname"] = _FFFcontrol.FFF_pdbname_get
    if _newclass:pdbname = _swig_property(_FFFcontrol.FFF_pdbname_get, _FFFcontrol.FFF_pdbname_set)
    __swig_setmethods__["nresidues"] = _FFFcontrol.FFF_nresidues_set
    __swig_getmethods__["nresidues"] = _FFFcontrol.FFF_nresidues_get
    if _newclass:nresidues = _swig_property(_FFFcontrol.FFF_nresidues_get, _FFFcontrol.FFF_nresidues_set)
    __swig_setmethods__["natoms"] = _FFFcontrol.FFF_natoms_set
    __swig_getmethods__["natoms"] = _FFFcontrol.FFF_natoms_get
    if _newclass:natoms = _swig_property(_FFFcontrol.FFF_natoms_get, _FFFcontrol.FFF_natoms_set)
    __swig_setmethods__["atomcounter"] = _FFFcontrol.FFF_atomcounter_set
    __swig_getmethods__["atomcounter"] = _FFFcontrol.FFF_atomcounter_get
    if _newclass:atomcounter = _swig_property(_FFFcontrol.FFF_atomcounter_get, _FFFcontrol.FFF_atomcounter_set)
    __swig_setmethods__["rescounter"] = _FFFcontrol.FFF_rescounter_set
    __swig_getmethods__["rescounter"] = _FFFcontrol.FFF_rescounter_get
    if _newclass:rescounter = _swig_property(_FFFcontrol.FFF_rescounter_get, _FFFcontrol.FFF_rescounter_set)
    __swig_setmethods__["last_resnum"] = _FFFcontrol.FFF_last_resnum_set
    __swig_getmethods__["last_resnum"] = _FFFcontrol.FFF_last_resnum_get
    if _newclass:last_resnum = _swig_property(_FFFcontrol.FFF_last_resnum_get, _FFFcontrol.FFF_last_resnum_set)
    __swig_setmethods__["all_atoms"] = _FFFcontrol.FFF_all_atoms_set
    __swig_getmethods__["all_atoms"] = _FFFcontrol.FFF_all_atoms_get
    if _newclass:all_atoms = _swig_property(_FFFcontrol.FFF_all_atoms_get, _FFFcontrol.FFF_all_atoms_set)
    __swig_setmethods__["_titratable_groups"] = _FFFcontrol.FFF__titratable_groups_set
    __swig_getmethods__["_titratable_groups"] = _FFFcontrol.FFF__titratable_groups_get
    if _newclass:_titratable_groups = _swig_property(_FFFcontrol.FFF__titratable_groups_get, _FFFcontrol.FFF__titratable_groups_set)
    __swig_setmethods__["BOXLJ"] = _FFFcontrol.FFF_BOXLJ_set
    __swig_getmethods__["BOXLJ"] = _FFFcontrol.FFF_BOXLJ_get
    if _newclass:BOXLJ = _swig_property(_FFFcontrol.FFF_BOXLJ_get, _FFFcontrol.FFF_BOXLJ_set)
    __swig_setmethods__["BOX10A"] = _FFFcontrol.FFF_BOX10A_set
    __swig_getmethods__["BOX10A"] = _FFFcontrol.FFF_BOX10A_get
    if _newclass:BOX10A = _swig_property(_FFFcontrol.FFF_BOX10A_get, _FFFcontrol.FFF_BOX10A_set)
    __swig_setmethods__["_pH"] = _FFFcontrol.FFF__pH_set
    __swig_getmethods__["_pH"] = _FFFcontrol.FFF__pH_get
    if _newclass:_pH = _swig_property(_FFFcontrol.FFF__pH_get, _FFFcontrol.FFF__pH_set)
    __swig_destroy__ = _FFFcontrol.delete_FFF
    __del__ = lambda self : None;
FFF_swigregister = _FFFcontrol.FFF_swigregister
FFF_swigregister(FFF)

class FFFError(Exception):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FFFError, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FFFError, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _FFFcontrol.new_FFFError()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _FFFcontrol.delete_FFFError
    __del__ = lambda self : None;
FFFError_swigregister = _FFFcontrol.FFFError_swigregister
FFFError_swigregister(FFFError)

class model_class(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, model_class, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, model_class, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _FFFcontrol.new_model_class(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _FFFcontrol.delete_model_class
    __del__ = lambda self : None;
    def get_chain_and_residue(self, *args): return _FFFcontrol.model_class_get_chain_and_residue(self, *args)
    def Mutate(self, *args): return _FFFcontrol.model_class_Mutate(self, *args)
    def Mutate_2(self, *args): return _FFFcontrol.model_class_Mutate_2(self, *args)
    def mutate_special(self, *args): return _FFFcontrol.model_class_mutate_special(self, *args)
    def undo_mutation(self): return _FFFcontrol.model_class_undo_mutation(self)
    def simple_mutate(self, *args): return _FFFcontrol.model_class_simple_mutate(self, *args)
    def setchi(self, *args): return _FFFcontrol.model_class_setchi(self, *args)
    def getchi(self, *args): return _FFFcontrol.model_class_getchi(self, *args)
    def getnumchi(self, *args): return _FFFcontrol.model_class_getnumchi(self, *args)
    def _get_atom(self, *args): return _FFFcontrol.model_class__get_atom(self, *args)
    def resolve_clashes(self): return _FFFcontrol.model_class_resolve_clashes(self)
    def _get_prev_residue(self, *args): return _FFFcontrol.model_class__get_prev_residue(self, *args)
    def _get_next_residue(self, *args): return _FFFcontrol.model_class__get_next_residue(self, *args)
    def getphi(self, *args): return _FFFcontrol.model_class_getphi(self, *args)
    def getpsi(self, *args): return _FFFcontrol.model_class_getpsi(self, *args)
    def calc_phi(self, *args): return _FFFcontrol.model_class_calc_phi(self, *args)
    def calc_psi(self, *args): return _FFFcontrol.model_class_calc_psi(self, *args)
    def calc_chi(self, *args): return _FFFcontrol.model_class_calc_chi(self, *args)
    def update_bonds(self, *args): return _FFFcontrol.model_class_update_bonds(self, *args)
    def repair_all(self): return _FFFcontrol.model_class_repair_all(self)
    def find_bad_residues(self): return _FFFcontrol.model_class_find_bad_residues(self)
    def find_missing_atoms(self, *args): return _FFFcontrol.model_class_find_missing_atoms(self, *args)
    __swig_setmethods__["unknown_residues"] = _FFFcontrol.model_class_unknown_residues_set
    __swig_getmethods__["unknown_residues"] = _FFFcontrol.model_class_unknown_residues_get
    if _newclass:unknown_residues = _swig_property(_FFFcontrol.model_class_unknown_residues_get, _FFFcontrol.model_class_unknown_residues_set)
    def build_hydrogens(self): return _FFFcontrol.model_class_build_hydrogens(self)
    def delete_all_hydrogens(self): return _FFFcontrol.model_class_delete_all_hydrogens(self)
    def delete_hydrogens(self, *args): return _FFFcontrol.model_class_delete_hydrogens(self, *args)
    def get_energy(self, *args): return _FFFcontrol.model_class_get_energy(self, *args)
    def get_soup_energy(self): return _FFFcontrol.model_class_get_soup_energy(self)
    def get_accessibility(self, *args): return _FFFcontrol.model_class_get_accessibility(self, *args)
    def assign_all_charges_and_radii(self): return _FFFcontrol.model_class_assign_all_charges_and_radii(self)
    __swig_setmethods__["_P"] = _FFFcontrol.model_class__P_set
    __swig_getmethods__["_P"] = _FFFcontrol.model_class__P_get
    if _newclass:_P = _swig_property(_FFFcontrol.model_class__P_get, _FFFcontrol.model_class__P_set)
    __swig_setmethods__["_crgrad"] = _FFFcontrol.model_class__crgrad_set
    __swig_getmethods__["_crgrad"] = _FFFcontrol.model_class__crgrad_get
    if _newclass:_crgrad = _swig_property(_FFFcontrol.model_class__crgrad_get, _FFFcontrol.model_class__crgrad_set)
    __swig_setmethods__["_use_hydrogens"] = _FFFcontrol.model_class__use_hydrogens_set
    __swig_getmethods__["_use_hydrogens"] = _FFFcontrol.model_class__use_hydrogens_get
    if _newclass:_use_hydrogens = _swig_property(_FFFcontrol.model_class__use_hydrogens_get, _FFFcontrol.model_class__use_hydrogens_set)
model_class_swigregister = _FFFcontrol.model_class_swigregister
model_class_swigregister(model_class)

class Rotamer_class(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Rotamer_class, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Rotamer_class, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _FFFcontrol.new_Rotamer_class(*args)
        try: self.this.append(this)
        except: self.this = this
    def get_rotamers(self, *args): return _FFFcontrol.Rotamer_class_get_rotamers(self, *args)
    __swig_setmethods__["_names"] = _FFFcontrol.Rotamer_class__names_set
    __swig_getmethods__["_names"] = _FFFcontrol.Rotamer_class__names_get
    if _newclass:_names = _swig_property(_FFFcontrol.Rotamer_class__names_get, _FFFcontrol.Rotamer_class__names_set)
    __swig_destroy__ = _FFFcontrol.delete_Rotamer_class
    __del__ = lambda self : None;
Rotamer_class_swigregister = _FFFcontrol.Rotamer_class_swigregister
Rotamer_class_swigregister(Rotamer_class)

class pKa_class(model_class):
    __swig_setmethods__ = {}
    for _s in [model_class]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, pKa_class, name, value)
    __swig_getmethods__ = {}
    for _s in [model_class]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, pKa_class, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _FFFcontrol.new_pKa_class(*args)
        try: self.this.append(this)
        except: self.this = this
    def find_titratable_groups(self): return _FFFcontrol.pKa_class_find_titratable_groups(self)
    def calculate_fractional_charge(self, *args): return _FFFcontrol.pKa_class_calculate_fractional_charge(self, *args)
    def calculate_titration_curves(self, *args): return _FFFcontrol.pKa_class_calculate_titration_curves(self, *args)
    __swig_destroy__ = _FFFcontrol.delete_pKa_class
    __del__ = lambda self : None;
pKa_class_swigregister = _FFFcontrol.pKa_class_swigregister
pKa_class_swigregister(pKa_class)



