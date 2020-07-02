# includes content from:
# https://www.tutorialspoint.com/downloading-files-from-web-using-python

from pathlib import Path
import re
import requests
import configparser
from cmascience.definitions import ROOT_DIR
from cmascience.io.filename_from_url import return_filename

# from cmascience.io.
from cmascience.io.read_input_source import read_input_source_ini

config = configparser.ConfigParser()
configfile = f"{ROOT_DIR}/cmascience/config.ini"
config.read(configfile)
inputs = config.get("DATADIR", "INPUTS")
inputdir= f"{ROOT_DIR}/{inputs}"

DEBUG=True

CMASCIENCE = Path(__file__).resolve().parents[2]


def download_input_data():
    codes = []
    for url in read_input_source_ini():
        resp = requests.get(url, allow_redirects=True)
        # open file and write the contents
        filename = return_filename(url)
        outfile = CMASCIENCE / "data" / "inputs" / filename
        if DEBUG:
            print(url)
            print(outfile)
        with open(outfile, "wb") as code:
            code.write(resp.content)
        codes.append(resp.status_code)
    return codes
