#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# from distutils.core import setup
# from Cython.Build import cythonize
# setup( ext_modules = cythonize('main_cy.pyx') )

from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy as np

file_name = 'main_cy'
extension = Extension(file_name, sources=[file_name+'.pyx'], language='c', include_dirs=[np.get_include()], library_dirs=[], libraries=[], extra_compile_args=[], extra_link_args=[] )
ext_modules = cythonize(extension)
setup(ext_modules = ext_modules)