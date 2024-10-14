import pytest

from example_pathlib_resources.paths import data_path_1, data_path_2
from example_pathlib_resources.some_module import read_data


@pytest.mark.xfail(raises=FileNotFoundError)
def test_read_data():
    data = read_data(data_path_1)
    assert data == "this is some data"


@pytest.mark.xfail(raises=AssertionError)
def test_data_pathsexists():
    f = data_path_1 / "some_data.txt"
    assert f.exists()


def test_read_data2():
    data = read_data(data_path_2)
    assert data == "this is some data\n"


def test_data_pathsexists2():
    f = data_path_2 / "some_data.txt"
    assert f.exists()
