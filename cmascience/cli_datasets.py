# resources
# https://stackoverflow.com/questions/7498595/python-argparse-add-argument-to-multiple-subparsers
# https://stackoverflow.com/questions/33645859/how-to-add-common-arguments-to-argparse-subcommands
# http://www.chiark.greenend.org.uk/doc/python3/html/library/argparse.html
# https://sphinx-argparse.readthedocs.io/en/stable/sample.html
# https://stackoverflow.com/questions/60209079/how-to-test-if-name-main-with-passing-command-line-arguments?noredirect=1&lq=1

"""

Command line application tool for CMASCIENCE

Lists HadObs observation datasets

"""

import argparse
import pkg_resources
import sys

import pandas as pd

from cmascience.cli.cli_observations_datasets import pick, all

# command line interface / command line application
# cli tool to list all observations datasets, or subdivided by marine or land

# used in the form

# python cli_datasets.py [command] [options] argument

# commands: all (list all) or pick (random)
# options:  limit the selection to netcdf
# argument:  dataset (marine, land, blended)

# the output is a printout of the pandas dataframe object

DEBUG = True

# Take the version number from the package version in setup
pkg_version = pkg_resources.get_distribution("cmascience").version


def cli_parent_parser() -> argparse.ArgumentParser:
    """Factory function to create parent parser for arguments from the command line """

    # Create parent parser object. Parent is used to ensure common arguments for optional subcommands
    parent_parser = argparse.ArgumentParser(prog='CMASCIENCE',
                                            epilog='  ---  ',
                                            add_help=False)
    # add_help=False is used to avoid conflict with subparsers, when parents is used to inherit options
    # https://docs.python.org/3/library/argparse.html#parents

    # Returns a parser object, with the metadata set
    return parent_parser



def cli_parent_arguments(parent_parser) -> argparse.ArgumentParser:
    """Adds cli parent parser arguments """

    # Arguments in argparse can be optional, positional or required, set to required to force user input
    # Add named arguments (required for the tool to run)

    # Set optional flag to show the app version
    parent_parser.add_argument('--version',
                               action='version',
                               help='Display the current version of the package',
                               version=f'{parent_parser.prog} {pkg_version}')

    # Set optional argument flag
    parent_parser.add_argument('--netcdf',
                               action='store_true',
                               help='Limit selection to netcdf datasets only')


    # Returns a parser object, with the arguments set
    return parent_parser



def cli_parser(parent_parser) -> argparse.ArgumentParser:
    """Factory function to create parser and subparser for arguments from the command line """

    parser = argparse.ArgumentParser(
        prog='CMASCIENCE',
        description=f'A simple app to list CMA observations datasets. Version {pkg_version}',
        epilog='  ---  ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        parents=[parent_parser])

    # Set the positional argument name
    parser.add_argument('dataset',
                               default='blended',
                               choices=['blended', 'marine', 'land'],
                               nargs='?', # specify number of arg, required to ensure default is applied
                               help='Type of dataset to select')
    # Add subparser to hold the subcommands
    subparsers = parser.add_subparsers(title='sub-commands',
                                       description='Valid sub-commands',
                                       help='Choose the data selection method',
                                       dest='Subcommand',
                                       required=True)

    # Set the subcommand names - by using subparsers
    all_parser = subparsers.add_parser('all',
                                       help='List all categories of datasets',
                                       parents=[parent_parser])
    pick_parser = subparsers.add_parser('pick',
                                        help='Pick one example dataset category at random',
                                        parents=[parent_parser])

    # Use set defaults so that each subparser knows which Python function it should execute
    all_parser.set_defaults(func=all)
    pick_parser.set_defaults(func=pick)

    return parser


def cli_parse_args(argv=None) -> argparse.Namespace:
    """
    Function to parse the passed arguments into an argparse namespace object
    :param argv:
    :return: argpase.Namespace


    """

    # Add the arguments
    parent_parser_with_arguments = cli_parent_arguments(cli_parent_parser())

    # Add the subparser commands
    main_parser = cli_parser(parent_parser_with_arguments)

    # Parse the arguments
    # ArgumentParser.parse_args processes whatever list of strings you pass it.
    # When you pass None, it uses sys.argv[1:] instead
    # This allows testing

    return main_parser.parse_args(argv)


def cli_datasets_entry_point(argv=None) -> pd.DataFrame:

    """
    Function to wrap passing the parsed command line arguments to
    the cli tool function

    :param argv:
    :return: None
    """

    # Read arguments from the command line
    # Parsed arguments are present as object attributes
    # Pass the parsed arguments to the cli analysis function
    parsed_args = cli_parse_args(argv)

    if DEBUG:
        print(parsed_args)
    # Call the default function, based on the command arguments passed
    output = parsed_args.func(parsed_args)

    if output.empty:
        print('Search criteria returned no datasets')
        return None

    return output


if __name__ == '__main__':

    if DEBUG:
        print('------')
        print(f'Number of arguments:', len(sys.argv), 'arguments.')
        print(f'Argument List:', str(sys.argv))
        print('------')

    cli_datasets_entry_point()