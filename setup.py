from setuptools import setup
from setuptools.extension import Extension

try:
    import cython  # noqa
    import numpy as np
    from Cython.Build import cythonize

    include_dirs = [np.get_include(), "cython_fortran_file"]
except ImportError:
    raise ImportError(
        """Could not import cython or numpy. Building this package from source requires
cython and numpy to be installed. Please install these packages using
the appropriate package manager for your python environment."""
    )


def read_readme():
    with open("Readme.md") as f:
        return f.read()


cython_extensions = [
    Extension(
        "cython_fortran_file.cython_fortran_utils",
        ["cython_fortran_file/cython_fortran_utils.pyx"],
        include_dirs=include_dirs,
    )
]


setup(ext_modules=cythonize(cython_extensions))
