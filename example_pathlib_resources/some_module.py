from pathlib import Path

from example_pathlib_resources.paths import data_path_1


def read_data(data_path: Path) -> str:
    with open(data_path / "some_data.txt") as f:
        data = f.read()

    return data
