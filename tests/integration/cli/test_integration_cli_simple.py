""" Test the cli_simple tool outputs
"""


import argparse
from pathlib import Path

from cmascience.cli_simple import cli_simple_entry_point

from cmascience.definitions import ROOT_DIR

# Define cli filepath
CLI = Path(ROOT_DIR, 'cmascience','cli_simple.py')


def test_cli_simple_entry_point():
    """Test for cli tool integration """

    # Create test arguments
    user_args = ['--x', '1', '--y', '2']

    # Apply cli tool to the arguments
    output = cli_simple_entry_point(user_args)

    # Confirm output is as expected
    # Expect output as the sum of the input values
    assert output == 2