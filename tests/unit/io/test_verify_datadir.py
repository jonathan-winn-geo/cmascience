from pathlib import Path

from cmascience.io.verify_datadir import datadir


def test_datadir():
    result = datadir()
    # assert Path(result).is_dir()
    assert result.is_dir()
    print(result)
