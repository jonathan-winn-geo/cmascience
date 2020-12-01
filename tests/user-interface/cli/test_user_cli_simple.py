""" Test the cli_simple tool at the user interface
"""

# Note cli is also tested via unit tests and integration tests

import subprocess
from pathlib import Path
import pytest

from cmascience.cli_simple import cli_parser, cli_parse_args, cli_analysis, cli_simple_entry_point
from cmascience.definitions import ROOT_DIR

# Define cli filepath
CLI = Path(ROOT_DIR, 'cmascience','cli_simple.py')
MODULE='cmascience.cli_simple'
#ENTRYPOINT=Path(ROOT_DIR, 'cmascience','cli_simple.cli_simple_entry_point')


def test_cli_simple_help_from_path():
    """
    Test cli can be run via Python from full path

    uses call to --help option to test cli tool is working
    """

    user_args = '--help'
    # Call the cli script via python and assign response
    out = subprocess.run(["python3", str(CLI), user_args], check=True)

    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0


def test_cli_simple_args_from_path():
    """
    Test of cli tool with args from full path

    uses call with arguments set to test cli tool
    """
    user_arg_x = '--x=1'
    user_arg_y = '--y=2'
    # Call the cli script via python - with args,  and assign response
    out = subprocess.run(["python3", str(CLI), user_arg_x, user_arg_y], check=True)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0


def test_cli_simple_run_as_module():
    """
    Tests if the cli tool can be run as a named Python module

    uses call to --help option to test cli tool is working
    """

    # Call the cli script via python as named module  and assign response
    out = subprocess.run(["python3", '-m', MODULE, '--help'], check=True)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0


def test_cli_simple_function_run():
    """
    Tests if the cli tool entry point function can be run as a named Python function

    uses call to --help option to test cli tool is working
    """

    # Call the cli script via python as named module  and assign response
    out = subprocess.run(['python3', '-c', '"from cmascience.cli_simple import cli_simple_entry_point; cli_simple_entry_point()"', '--help'], check=True)

    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0



def test_cli_simple_run_as_entrypoint():
    """
    Tests if the entrypoint script can be called by name

    tests that it has been installed? (via setup.py)
    """

    # Call the cli tool by script name
    # The name is set by the entry_points section of setup.py
    out = subprocess.run(['cli-simple', '--help'], check=True)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0

def test_cli_system_args():
    """
    Test how sys argv are passed
    :return:
    """

    import sys

    # print
    # 'Number of arguments:', len(sys.argv), 'arguments.'
    # print
    # 'Argument List:', str(sys.argv)

    # Call the cli tool by script name
    # The name is set by the entry_points section of setup.py
    out = subprocess.run(['cli-simple', '--help'], check=True)
    #print(out.sys.argv)
    print(out.args)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0



# Run a range of tests to check that accessing and using the cli tool behaves as expected
# Returns error or fails if the user gives the wrong values

def test_cli_simple_run_as_module_with_options():
    """
    Tests if the cli tool can be run as a named Python module

    uses call to --help option to test cli tool is working
    """

    # Call the cli script via python as named module  and assign response
    out = subprocess.run(["python3",
                          '-m',
                          MODULE,
                          '--x',
                          '5',
                          '--y',
                          '3'],
                         check=True)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0



def test_cli_simple_entry_point_user_input():
    """Test for cli tool user input values """

    # Create a range of possible user input test arguments
    value_too_large = ['--x', '1000000000', '--y', '-2']
    value_too_small = ['--x', '2', '--y', '-2']
    argument_missing = ['--x', '1']
    too_many_arguments = ['--x', '4', '--y', '2', '--z', '3']

    # Apply cli tool
    # Confirm expected errors - expect to fail
    with pytest.raises(SystemExit):
        cli_simple_entry_point(value_too_small)

    with pytest.raises(SystemExit):
        cli_simple_entry_point(value_too_large)

    with pytest.raises(SystemExit):
      cli_simple_entry_point(argument_missing)

    with pytest.raises(SystemExit):
      cli_simple_entry_point(too_many_arguments)