# Script to example test dataset of HadObs observations datasetsc

"""

Create csv output files holding mock up static list of HadObs datasets (for use with CLI tool)

"""

import sys
import pkg_resources

import pandas as pd
from pathlib import Path

from cmascience.definitions import ROOT_DIR

DEBUG = True

# Input data ready for pandas dataframe

# Note - this is a mocked up dataset list, although based on HadObs it is just for training purposes

data = {'dataset':
            ['HadISST', 'HadSST3', 'HadSST4', 'HadNMAT2', 'EN4', 'HadCRUT4', 'HadCRUH', 'data8'],
        'latest':
            ['1.1', '3.1.1.0', '4.0.0.0', '2.0.1.0', '4.2.1', '4.6.0.0', '1', '1'],
       'category':
           ['marine', 'marine', 'marine', 'marine', 'marine', 'blended', 'blended', 'land'],
       'format':
            ['netcdf', 'netcdf', 'netcdf', 'netcdf', 'zip', 'netcdf', 'netcdf', 'txt']
       }

df = pd.DataFrame(data)

filename = 'observation_data.csv'
outfile = Path(ROOT_DIR) / 'data' / 'reference' / filename


def write_csv_data(df, outfile):
    """ Write pandas dataframe to output csv file

    :param args:
    :return:
    """

    df.to_csv(outfile, encoding='utf-8', index=False)


if __name__ == '__main__':

    if DEBUG:
        print('------')
        print(f'Writing test data to:', outfile)
        print('------')

    write_csv_data(df, outfile)