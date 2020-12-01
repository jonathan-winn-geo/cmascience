"""

Command line application tool for SIMPLE

Allows development and testing of a simple command line tool

"""

import argparse
import pkg_resources
import sys

DEBUG = True

# Take the version number from the package version in setup
pkg_version = pkg_resources.get_distribution("cmascience").version



def cli_parser() -> argparse.ArgumentParser:
    """Factory function to create parser for arguments from the command line """

    parser = argparse.ArgumentParser(
        # Adds cli app title, if ommitted the filename is used (e.g. cli-simple.py)
        prog='CLI-SIMPLE',
        description=f'A simple app',
        epilog='  ---  ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Returns a parser object, with the metadata and arguments set
    return parser

def cli_arguments(parser) -> argparse.ArgumentParser:
    """Adds cli tool arguments """

    # Arguments in argparse can be optional, positional or required, set to required to force user input
    # Add named arguments (required for the tool to run)
    # Set the argument type (e.g. int) and limit choices from a list
    parser.add_argument("--x", type=int, help="the x value", required=True, choices=[0,1,2,3,4,5])
    parser.add_argument("--y", type=int, help="the y value", required=True, choices=[0,1,2,3,4,5])

    # Returns a parser object, with the arguments set
    return parser

def cli_parse_args(argv=None) -> argparse.Namespace:
    """
    Function to parse the passed arguments into an argparse namespace object
    :param argv:
    :return: argpase.Namespace


    """

    # Instantiate cli parser object
    parser = cli_parser()

    # Add the arguments
    cli_arguments(parser)

    # Parse the arguments
    # ArgumentParser.parse_args processes whatever list of strings you pass it.
    # When you pass None, it uses sys.argv[1:] instead
    # This allows testing

    return parser.parse_args(argv)

def cli_analysis(parsed_args):

    """
    Function to run simple sum analysis on the passed x and y arguments
    Analysis is the sum of x and y

    :param parsed_args:
    :return:
    """

    # The main functionality of the cli tool - just sums the x and y values
    analysis_sum = parsed_args.x * parsed_args.y

    if DEBUG:
        print(parsed_args)
        # Simple print to show the cli tool is working
        print('The cli tool: SIMPLE has run')
        print(f'The x value is: {parsed_args.x}')
        print(f'The y value is: {parsed_args.y}')
        print(f'The sum is: {analysis_sum}')

    return analysis_sum


def cli_simple_entry_point(argv=None):
#def cli_simple_entry_point():

    """
    Function to wrap passing the parsed command line arguments to
    the analysis function

    :param argv:
    :return: None
    """
    # if DEBUG:
    #     print('------')
    #     #print(f'argv: ', argv)
    #     print('------')
    #     print(f'Number of arguments:', len(sys.argv), 'arguments.')
    #     print(f'Argument List:', str(sys.argv))


    # Read arguments from the command line
    # Parsed arguments are present as object attributes
    # Pass the parsed arguments to the cli analysis function
    #result = cli_analysis(cli_parse_args())
    result = cli_analysis(cli_parse_args(argv))
    return result

if __name__ == '__main__':
    # Runs entry point function when called as main
    cli_simple_entry_point()
    if DEBUG:
        print('------')
        print(f'Number of arguments:', len(sys.argv), 'arguments.')
        print(f'Argument List:', str(sys.argv))
        print('------')
