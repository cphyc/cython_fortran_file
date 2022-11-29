import numpy as np
from Cython.Build import cythonize
from setuptools import setup
from setuptools.extension import Extension

include_dirs = [np.get_include(), "cython_fortran_file"]

cython_extensions = [
    Extension(
        "cython_fortran_file.cython_fortran_utils",
        ["cython_fortran_file/cython_fortran_utils.pyx"],
        include_dirs=include_dirs,
    )
]


setup(ext_modules=cythonize(cython_extensions))
