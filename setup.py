# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.extension import Extension

# with open('Readme.md') as f:
#     readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

cython_extensions = [
    Extension("cython_fortran_file",
              ["src/cython_fortran_utils.pyx"],
              include_dirs=['src'])
]
setup(
    name='cython_fortran_file',
    version='0.0.1',
    description='An efficient way of reading fortran-record files.',
    # long_description=readme,
    classifiers=[
        'Development status :: 1 - Alpha',
        'License :: CC-By-SA2.0',
        'Programming Language :: Python',
        'Topic :: Fortran'
    ],
    author='Corentin Cadiou',
    author_email='contact@cphyc.me',
    url='https://github.com/cphyc/cython-fortran-file',
    license=license,
    packages=['src'],
    install_requires=[
        'cython',
        'numpy'
    ],
    ext_modules=cython_extensions
)
