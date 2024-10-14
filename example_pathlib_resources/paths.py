from importlib.resources import files
from pathlib import Path


data_path_1 = Path("./data")
data_path_2 = files("example_pathlib_resources.data")
