""" Test the cli_analysis tool at the user interface
"""

# Note cli is also tested via unit tests and integration tests

import subprocess
from pathlib import Path
import pytest

from cmascience.cli_datasets import cli_datasets_entry_point
from cmascience.definitions import ROOT_DIR

# Define cli filepath
CLI = Path(ROOT_DIR, 'cmascience','cli_datasets.py')
MODULE='cmascience.cli_datasets'


def test_cli_help_from_path():
    """
    Test cli can be run via Python from full path

    uses call to --help option to test cli tool is working
    """

    user_args = '--help'
    # Call the cli script via python and assign response
    out = subprocess.run(["python3", str(CLI), user_args], check=True)

    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0


def test_cli_args_from_path():
    """
    Test of cli tool with args from full path

    uses call with arguments set to test cli tool
    """
    user_arg_x = 'land'
    user_arg_y = 'all'
    # Call the cli script via python - with args,  and assign response
    out = subprocess.run(["python3", str(CLI), user_arg_x, user_arg_y], check=True)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0

def test_cli_run_as_module():
    """
    Tests if the cli tool can be run as a named Python module

    uses call to --help option to test cli tool is working
    """

    # Call the cli script via python as named module  and assign response
    out = subprocess.run(["python3", '-m', MODULE, '--help'], check=True)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0

def test_cli_function_run():
    """
    Tests if the cli tool entry point function can be run as a named Python function

    uses call to --help option to test cli tool is working
    """

    # Call the cli script via python as named module  and assign response
    out = subprocess.run(['python3',
                          '-c',
                          '"from cmascience.cli_datasets import cli_datasets_entry_point; cli_datasets_entry_point()"',
                          '--help'],
                         check=True)

    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0


def test_cli_datasets_run_as_entrypoint():
    """
    Tests if the entrypoint script can be called by name

    tests that it has been installed? (via setup.py)
    """

    # Call the cli tool by script name
    # The name is set by the entry_points section of setup.py
    out = subprocess.run(['cli-datasets', '--help'], check=True)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0

    out = subprocess.run(['cli-datasets', 'land', 'all'], check=True)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0

    # cli tool will run with one subcommand argument, as the main input has a default value, so is optional
    out = subprocess.run(['cli-datasets', 'all'], check=True)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0

    # Whne both the positional argument and subcommand are present, the positional argument must be first
    out = subprocess.run(['cli-datasets', 'land', 'all', '--netcdf'], check=True)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0

    # The optional netcdf argument can occur in any order
    out = subprocess.run(['cli-datasets', '--netcdf', 'land', 'pick'], check=True)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0


# START #

# still problems with the tests, are te subparpsers and main parsers working ok ?
# mainly defauls to blended, even when positional argument given


def test_cli_run_as_module_with_options():
    """
    Tests if the cli tool can be run as a named Python module - with arguments

    """

    # Call the cli script via python as named module  and assign response
    out = subprocess.run(["python3", '-m', MODULE, 'land', 'all'], check=True)
    # Check if exit code indicates success (0 = success)
    assert out.returncode == 0


# Run a range of tests to check that accessing and using the cli tool behaves as expected
# Returns error or fails if the user gives the wrong values

def test_cli_datasets_entry_point_user_input():
    """Test for cli tool user input values """

    # Create a range of possible user input test arguments - expected to fail
    wrong_argument_order = ['--netcdf', 'all', 'land']
    missing_subcommand = ['land']
    argument_missing = ['']
    too_many_arguments = ['land', 'all', '--netcdf', 'marine']

    # Apply cli tool
    # Confirm expected errors - expect to fail
    with pytest.raises(SystemExit):
        cli_datasets_entry_point(wrong_argument_order)

    with pytest.raises(SystemExit):
        cli_datasets_entry_point(missing_subcommand)

    with pytest.raises(SystemExit):
        cli_datasets_entry_point(argument_missing)

    with pytest.raises(SystemExit):
        cli_datasets_entry_point(too_many_arguments)



