import os
from pathlib import Path

import configparser
from cmascience.definitions import ROOT_DIR


config = configparser.ConfigParser()
configfile = f"{ROOT_DIR}/cmascience/config.ini"
config.read(configfile)
root = config.get("DATADIR", "ROOT")

DEBUG = False


def return_root_dir():
    test_dir = os.path.expanduser(root)
    if DEBUG:
        print(root)
        print(test_dir)
    return test_dir
