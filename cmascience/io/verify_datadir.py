import configparser
from pathlib import Path

from cmascience.io.read_root_dir import return_root_dir
from cmascience.definitions import ROOT_DIR

config = configparser.ConfigParser()
configfile = f"{ROOT_DIR}/cmascience/config.ini"
config.read(configfile)
inputs = config.get("DATADIR", "INPUTS")
root_dir = return_root_dir()
inputdir= Path(root_dir)/inputs

DEBUG = True

def datadir():
    indir = inputdir.mkdir(parents=True, exist_ok=True)
    if DEBUG:
        print(root_dir)
        print(indir)
    return inputdir