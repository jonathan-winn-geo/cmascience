from pathlib import Path

from cmascience.io.read_root_dir import return_root_dir


def test_root_dir():
    result = return_root_dir()
    assert Path(result).is_dir()
    print(result)
