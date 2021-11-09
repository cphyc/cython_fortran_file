# Cython fortran-file

[![Build and Test](https://github.com/cphyc/cython_fortran_file/actions/workflows/build-test.yaml/badge.svg)](https://github.com/cphyc/cython_fortran_file/actions/workflows/build-test.yaml)
[![PyPI](https://img.shields.io/pypi/v/cython_fortran_file)](https://pypi.org/project/cython_fortran_file)
[![Conda-forge](https://img.shields.io/conda/vn/conda-forge/cython-fortran-file.svg)](https://anaconda.org/conda-forge/cython-fortran-file)

This package is a fast and easy reader for record-based binary format, as written by Fortran.

## Installation

This packages requires a compiler to be installed on you system. If you're using Linux or MacOSX you should be fine. If you're using Windows, please get in touch with me or open an issue.
```
pip install cython_fortran_file
```
That's all!

## Using it
Here is a simple demonstration:

```python
from cython_fortran_file import FortranFile as FF

f = FF("/path/to/my/fortran/file.dat", mode="r")

# Skip 5 records
f.skip(5)

# Read one record (an array of `double`)
data = f.read_vector("d")
assert data.dtype == np.float64

# Read one record (an array of signed `int`)
data = f.read_vector("i")
assert data.dtype == np.int32

# Read one *single* int. This will fail if there is more to read!
v = f.read_int()

# f _looks_ like a regular file descriptor
f.tell()
f.seek(0)
f.close()
```

It also supports `with` statement so that you can't forget to close the file handler
```python
with FF("/path/to/my/fortran/file.dat") as f:
    f.skip(5)

    data = f.read_vector("d")  # Read a vector of doubles (as usual)
```

## Data types

The argument of `read_vector` follows the convention of the python struct package (C convention). See https://docs.python.org/3.5/library/struct.html#format-characters for the full list. Here is a shorter version:

Argument | Fortran type | C type     | Numpy dtype
---------|--------------|------------|--------------
`d`      | `real(8)`    | `double`   | `np.float64`
`f`      | `real(4)`    | `float`    | `np.float32`
`i`      | `integer`    | `int`      | `np.int32`
`l`      | `integer(8)` | `long`     | `np.int64`
