# Script to amalgamate the indiv dataset metadata files into a summary files - catalogue

"""

Compile dataset metadata files

"""

import pandas as pd
from pathlib import Path

from cmascience.definitions import ROOT_DIR

DEBUG = True


hadobs = Path(ROOT_DIR) / 'data' / 'reference' / 'hadobs'

# add reader
# compile to summary
# summary stats

# TODO >>>>>>>>>>>>>>>>>>>
# Placeholder file -
# read in all yaml files in the hadbs dir and write out to df object or csv
# potentially replaces observation_data.csv


if __name__ == '__main__':

    if DEBUG:
        print('------')
        #print(f'Reading metadata from:', outfile)
        print('------')

