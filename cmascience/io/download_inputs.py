# includes content from:
# https://www.tutorialspoint.com/downloading-files-from-web-using-python
import os
from pathlib import Path
import re
import requests
import configparser
from cmascience.definitions import ROOT_DIR
from cmascience.io.filename_from_url import return_filename
from cmascience.io.read_root_dir import return_root_dir

# from cmascience.io.
from cmascience.io.read_input_source import read_input_source_ini

config = configparser.ConfigParser()
configfile = f"{ROOT_DIR}/cmascience/config.ini"
config.read(configfile)
inputs = config.get("DATADIR", "INPUTS")
root = return_root_dir()
inputdir = f"{root}/{inputs}"

DEBUG = True

# CMASCIENCE = Path(__file__).resolve().parents[2]


def download_input_data():
    codes = []
    for url in read_input_source_ini():
        resp = requests.get(url, allow_redirects=True)
        # open file and write the contents
        filename = return_filename(url)
        outfile = Path(inputdir) / filename
        if DEBUG:
            print("---!---")
            print(url)
            print(outfile)
            print("---!---")
        with open(outfile, "wb") as code:
            code.write(resp.content)
            if DEBUG:
                print(os.path.isfile(outfile))
                print(outfile.absolute())

        codes.append(resp.status_code)

    return codes
