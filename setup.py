# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.sdist import sdist as _sdist
from setuptools.extension import Extension
from Cython.Build import cythonize

with open('Readme.md') as f:
    readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

cython_extensions = [
    Extension("cython_fortran_file.cython_fortran_utils",
              ["cython_fortran_file/cython_fortran_utils.pyx"],
              include_dirs=['cython_fortran_file/'])
]

# class sdist(_sdist):
#     # subclass setuptools source distribution builder to ensure cython
#     # generated C files are included in source distribution.
#     # See http://stackoverflow.com/a/18418524/1382869
#     def run(self):
#         # Make sure the compiled Cython files in the distribution are
#         # up-to-date

#         # Make sure the compiled Cython files in the distribution are up-to-date
#         from Cython.Build import cythonize
#         cythonize(cython_extensions)


setup(
    name='cython_fortran_file',
    version='0.0.3',
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
