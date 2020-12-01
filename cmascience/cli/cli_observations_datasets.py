# resources
# https://stackoverflow.com/questions/7498595/python-argparse-add-argument-to-multiple-subparsers
# https://stackoverflow.com/questions/33645859/how-to-add-common-arguments-to-argparse-subcommands
# http://www.chiark.greenend.org.uk/doc/python3/html/library/argparse.html
# https://sphinx-argparse.readthedocs.io/en/stable/sample.html
# https://stackoverflow.com/questions/60209079/how-to-test-if-name-main-with-passing-command-line-arguments?noredirect=1&lq=1

"""

Main analysis function for the CMASCIENCE cli tool

"""

import pandas as pd
from pathlib import Path

from cmascience.definitions import ROOT_DIR

DEBUG = True

observations = 'observation_data.csv'
obsfile = Path(ROOT_DIR) / 'data' / 'reference' / observations



def observations(args) -> pd.DataFrame:
    """ Select and return the type of cma observation from user defined selection

    :param args:
    :return:
    """

    # Read the contents of csv file into pandas dataframe
    df = pd.read_csv(obsfile)

    # Select from the dataframe based on the input dataset category
    # df.loc Access a group of rows and columns by label(s) or a boolean array
    obs_selection = df.loc[df['category'] == args.dataset]
    # There should always be a selection, all data entries should have a category

    return obs_selection

def check_netcdf(args, obs_selection) -> pd.DataFrame:
    """ Check for netcdf flag and if present, select only netcdf records

    """

    if args.netcdf:
        obs_netcdf = obs_selection.loc[obs_selection['format'] == '.netcdf']
        return obs_netcdf
    else:
        return obs_selection

def all(args) -> pd.DataFrame:
    """ Return all the datasets, accounting for the netcdf option flags

    """
    return check_netcdf(args, observations(args))

def pick(args) -> pd.DataFrame:
    """ Return a single dataset, as a sample, accounting for the netcdf option flags

    """
    datasets = check_netcdf(args, observations(args))
    # Deal with cases where there is only 1 row in the dataframe (only 1 dataset matches the selection)
    if datasets.shape[0] is 0:
        return datasets
    else:
        # sample returns 1 value as default, using n=1 for clarity and testing of other values
        sample = datasets.sample(n=1)
        return sample
