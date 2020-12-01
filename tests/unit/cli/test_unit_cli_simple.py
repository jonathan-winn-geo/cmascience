""" Test the cli_simple tool
"""


import pytest
import inspect
import io
import subprocess
import argparse
from pathlib import Path
from contextlib import redirect_stdout

from cmascience.cli_simple import cli_parse_args, cli_parser, cli_analysis, cli_arguments

from cmascience.definitions import ROOT_DIR

# Define cli filepath
CLI = Path(ROOT_DIR, 'cmascience','cli_simple.py')

def test_cli_parser():

    """Test for cli_parser() function."""

    parser = cli_parser()
    # Confirm output object is correct parser type
    assert  isinstance(parser, argparse.ArgumentParser)
    # Confirm cli tool name is correct
    assert parser.prog == 'CLI-SIMPLE'
    # Confirm the cli tool has a text description
    assert isinstance(parser.description, str)
    # Confirm the cli tool has a text description

def test_cli_arguments():

    """Test for cli_arguments() function."""

    parser = cli_parser()
    parser_args = cli_arguments(parser)
    varlist = vars(parser_args)

    # TODO check any other test options using mock?
    # TODO strictly, move to integration tests
    # Not easily possible to test just that the arguments have been added and named without calling parser
    # One option below,
    # TODO, remove this, as covered by parse_args tests
    assert '--x' in varlist['_option_string_actions']
    assert '--y' in varlist['_option_string_actions']

    # Can also test via calling parse args
    parsed = parser_args.parse_args(['--x', '5', '--y', '4'])
    assert parsed.x == 5

def test_cli_parse_args():

    """Test for cli_parse_args() function"""

    # Set user input args and input values
    user_args = ['--x', '1', '--y', '2']

    parsed_args = cli_parse_args(user_args)

    # Check the parsed args are correctly stored in a namespace object
    assert isinstance(parsed_args, argparse.Namespace)

    # Confirm arguments names have been set
    assert 'x' in vars(parsed_args)
    assert 'y' in vars(parsed_args)

    # Confirm the argument values have been read back correctly
    assert parsed_args.x == 1
    assert parsed_args.y == 2

def test_cli_analysis():
    """Test for cli_analysis() function """

    # Create an argparse namespace object and assign values to arguments
    parsed_args = argparse.Namespace(x=1, y=2)

    # Run the analysis
    output = cli_analysis(parsed_args)

    # Confirm output is as expected
    # Expect output as the sum of the input values
    assert output == 2