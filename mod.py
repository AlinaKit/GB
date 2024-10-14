'''descript my modul
   __init__.py make package by directory with moduls
   __init__.py played when import
   from dir.mod import func as f1 : is path of function in module in directory and named function as f1 in thus file.
   may be dir1/
             __init__.py
             dir2/
                __init__.py
                module1
                module2
            dir3/
               __init__.py
               module3

    python .\1st_file_name.py arg1 arg2 argn : play script (module) in OS's therminal with args

'''

import random as rdm  # nessessary imports

all = ['func_1', 'change_1', 'change_n']  # access accept to read and use in "from smw import *"

CONST_1 = 111  # access accept to read and use in "from smw import *"
_name = 1  # access denyed to read and use in "from smw import *"
noname = 11  # access denyed to read and use in "from smw import *"


def func_1(*args):  # access accept to read and use in "from smw import *"
    z = 0  # access denyed to read and use in "from smw import *"
    print(z)


def func_2(*args):  # access denyed to read and use in "from smw import *"
    x = 0
    print(x)


print(f'{CONST_1 = }')  # will played when import

print(f'без сида - {rdm.random()}')
rdm.seed(1)
stt = rdm.getstate()
print(f'getstate - {rdm.random()}')
print(rdm.random())
print(rdm.random())
rdm.setstate(stt)
print(f'setstate - {rdm.random()}')
print(rdm.random())
print(rdm.random())
rdm.seed(5)
stt2 = rdm.getstate()
print(f'getstate - {rdm.random()}')
print(rdm.random())
print(rdm.random())
rdm.setstate(stt2)
print(f'setstate - {rdm.random()}')
print(rdm.random())
print(rdm.random())
rdm.setstate(stt)
print(f'setstate - {rdm.random()}')
print(rdm.random())
print(rdm.random())

if __name__ == 'main':  # wont played when import, only play from this file
    print(f'{CONST_1 = }/n{_name = }/n{__noname = }/n{func_1() = }/n{func_2() = }')