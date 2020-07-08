import configparser
from cmascience.definitions import ROOT_DIR

config = configparser.ConfigParser()

configfile = f"{ROOT_DIR}/cmascience/config.ini"


def read_input_source_ini():
    """Read input sources from the yaml file"""

    config.read(configfile)
    coasts = config.get("INPUTS", "COASTS")
    elevation = config.get("INPUTS", "ELEVATION")
    sst = config.get("INPUTS", "SST")

    return coasts, elevation, sst
