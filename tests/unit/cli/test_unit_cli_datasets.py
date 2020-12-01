""" Test the cli_datasets tool outputs
"""


import pytest
import inspect
import io
import subprocess
import argparse
from pathlib import Path
from contextlib import redirect_stdout

from cmascience.cli_datasets import cli_parse_args, cli_parser, cli_parent_parser, cli_parent_arguments, cli_datasets_entry_point

from cmascience.definitions import ROOT_DIR

# Define cli filepath
#CLI = Path(ROOT_DIR, 'cmascience','cli_simple.py')

DEBUG = True

def test_cli_parser():

    """Test for cli_parser() function."""

    parser = cli_parser(cli_parent_parser())
    # Confirm output object is correct parser type
    assert  isinstance(parser, argparse.ArgumentParser)
    # Confirm cli tool name is correct
    assert parser.prog == 'CMASCIENCE'

    # Confirm the cli tool has a text description
    assert isinstance(parser.description, str)

def test_cli_parent_parser():

    """Test for cli_parent_parser() function."""

    parser = cli_parent_parser()
    # Confirm output object is correct parser type
    assert  isinstance(parser, argparse.ArgumentParser)
    # Confirm cli tool name is correct
    assert parser.prog == 'CMASCIENCE'




def test_cli_parent_arguments():

    """Test for cli_parent_arguments() function."""

    # TODO edit down, move some of these to user interface tests

    parent_parser = cli_parent_parser()
    parser_args = cli_parent_arguments(parent_parser)

    parsed = parser_args.parse_args(['marine'])
    if DEBUG:
        print(parsed)
    assert parsed.dataset == 'marine'

    # If no arguments are passed, then default is used (default=blended)
    parsed = parser_args.parse_args([])
    if DEBUG:
        print(parsed)
    assert parsed.dataset == 'blended'

    # The netcdf flag argument is optional, a boolean flag
    parsed = parser_args.parse_args(['--netcdf'])
    if DEBUG:
        print(parsed)
    assert parsed.netcdf == True

    # The netcdf flag argument is optional, a boolean flag
    parsed = parser_args.parse_args(['land','--netcdf'])
    if DEBUG:
        print(parsed)
    assert parsed.netcdf == True
    assert parsed.dataset == 'land'


    # The version flag argument is optional
    # Calling version print to output and exist, cannot be assigned
    # TODO remove or fix
    # Leaving this here as just a visual print in test outputs of current cli tool / python package version

    try:
        parser_args.parse_args(['--version'])
    except SystemExit:
        pass








#  >>>>>> START HERE >>>>>>>


def test_cli_parse_args():

    """Test for cli_parse_args() function"""

    # Set user input args and input values

    user_args = ['all']
    parsed_args = cli_parse_args(user_args)
    if DEBUG:
        print(parsed_args)
    # Check the parsed args are correctly stored in a namespace object
    assert isinstance(parsed_args, argparse.Namespace)
    # Confirm the argument values have been read back correctly
    assert parsed_args.Subcommand == 'all'

    user_args = ['pick']
    parsed_args = cli_parse_args(user_args)
    if DEBUG:
        print(parsed_args)
    # Check the parsed args are correctly stored in a namespace object
    assert isinstance(parsed_args, argparse.Namespace)
    # Confirm the argument values have been read back correctly
    assert parsed_args.Subcommand == 'pick'



   # # Set user input args and input values
   #  user_args = ['--netcdf', 'all']
   #  parsed_args = cli_parse_args(user_args)
   #  # Check the parsed args are correctly stored in a namespace object
   #  assert isinstance(parsed_args, argparse.Namespace)
   #  # Confirm the argument values have been read back correctly
   #  assert parsed_args.Subcommand == 'all'
   #  assert parsed_args.dataset == 'blended'
   #  assert parsed_args.netcdf == True
   #  assert parsed_args.

   # Set user input args and input values
    user_args = ['pick','--netcdf']
    parsed_args_2 = cli_parse_args(user_args)
    if DEBUG:
        print(parsed_args_2)
    # Check the parsed args are correctly stored in a namespace object
    assert isinstance(parsed_args_2, argparse.Namespace)

    # Confirm the argument values have been read back correctly
    assert parsed_args_2.Subcommand == 'pick'
    assert parsed_args_2.netcdf == True


   # Set user input args and input values
    user_args = ['land','pick']
    parsed_args = cli_parse_args(user_args)
    if DEBUG:
        print(parsed_args)
    # Check the parsed args are correctly stored in a namespace object
    assert isinstance(parsed_args, argparse.Namespace)

    # Confirm the argument values have been read back correctly
    assert parsed_args.Subcommand == 'pick'
    assert parsed_args.dataset == 'land'


#def test_cli_analysis():
    # """Test for cli_analysis() function """
    #
    # # Create an argparse namespace object and assign values to arguments
    # parsed_args = argparse.Namespace(x=1, y=2)
    #
    # # Run the analysis
    # output = cli_analysis(parsed_args)
    #
    # # Confirm output is as expected
    # # Expect output as the sum of the input values
    # assert output == 2