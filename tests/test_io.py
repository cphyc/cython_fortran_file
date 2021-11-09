from pathlib import Path

import numpy as np

from cython_fortran_file import FortranFile

test_file = Path(__file__).parent / "testfile.bin"
test_file_attrs = Path(__file__).parent / "testfile_attrs.bin"
test_file_write = Path(__file__).parent / "testfile_write.bin"


def check_vector(f, expected, dtype):
    vec = f.read_vector(dtype)
    np.testing.assert_equal(vec, expected)


def test_reading():
    with FortranFile(test_file, mode="r") as f:
        assert f.read_int() == 1234
        assert f.read_int64() == 123456789
        check_vector(f, np.array([1.0], dtype="float32"), "float32")
        check_vector(f, np.array([2.0], dtype="float64"), "float64")

        check_vector(f, np.array([5, 6], dtype="int32"), "int32")
        check_vector(f, np.array([7, 8], dtype="int64"), "int64")
        check_vector(f, np.array([1.0, 2.0], dtype="float32"), "float32")
        check_vector(f, np.array([3.0, 4.0], dtype="float64"), "float64")


def test_reading_attrs():
    attrs = (
        ("first", 1, "i"),
        (("a", "b", "c", "d"), 4, "int32"),
        (("x1", "x2", "x3", "x4"), 4, "float64"),
        ("test", 4, "c"),
    )
    with FortranFile(test_file_attrs, mode="r") as f:
        ret = f.read_attrs(attrs)

    expected = {
        "first": 1,
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "x1": 1.0,
        "x2": 2.0,
        "x3": 3.0,
        "x4": 4.0,
        "test": np.array([b"t", b"e", b"s", b"t"], dtype="|S1"),
    }

    for key in expected.keys():
        exp = expected[key]
        obt = ret[key]

        np.testing.assert_equal(exp, obt)


def test_seeking():
    with FortranFile(test_file, mode="r") as f:
        f.skip(1)
        ipos = f.tell()
        f.skip(2)
        f.seek(ipos)


def test_writing():
    content = [
        np.random.randint(10, size=100).astype("int32"),
        np.random.randint(10, size=100).astype("int64"),
        np.random.rand(100).astype("float32"),
        np.random.rand(100).astype("float64"),
    ]
    with FortranFile(test_file_write, mode="w") as f:
        for c in content:
            f.write_vector(c)

    with FortranFile(test_file_write, mode="r") as f:
        for c in content:
            check_vector(f, c, str(c.dtype))
