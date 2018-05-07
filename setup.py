# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.sdist import sdist as _sdist
from setuptools.extension import Extension
from Cython.Build import cythonize

with open('Readme.md') as f:
    readme = f.read()

try:
    import numpy as np
    import cython
    include_dirs = [np.get_include(), 'cython_fortran_file']
except ImportError:
    raise ImportError(
"""Could not import cython or numpy. Building this package from source requires
cython and numpy to be installed. Please install these packages using
the appropriate package manager for your python environment.""")


cython_extensions = [
    Extension("cython_fortran_file.cython_fortran_utils",
              ["cython_fortran_file/cython_fortran_utils.pyx"],
              include_dirs=include_dirs)
]


setup(
    name='cython_fortran_file',
    version='0.0.7',
    description='An efficient package to read fortran-record files in Python.',
    long_description=readme,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    author='Corentin Cadiou',
    author_email='contact@cphyc.me',
    url='https://github.com/cphyc/cython-fortran-file',
    license=license,
    packages=find_packages(),
    package_data={
        'cython_fortran_file': ['cython_fortran_file/*.pyx',
                                'cython_fortran_file/*.pxd'],
    },
    install_requires=[
        'cython',
        'numpy'
    ],
    ext_modules=cythonize(cython_extensions)
)
