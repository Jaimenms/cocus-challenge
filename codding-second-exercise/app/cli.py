import argparse
import os
import sys
from enum import Enum, unique

# Parameters
INITIAL_NUMBER_OF_FRUITS = 50
NUMBER_OF_PICKER_WORKERS = 3
NUMBER_OF_CLEANER_WORKERS = 2


class Parser:
    """
    A class used to encapsulate all the methods of the CLI parser in different versions
    """

    @staticmethod
    def get_v1() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description="Executes the farming simulator")
        parser.add_argument(
            '--pickers',
            type=int,
            help=f"Number of pickers [Default: {NUMBER_OF_PICKER_WORKERS}]",
            default=NUMBER_OF_PICKER_WORKERS
        )
        parser.add_argument(
            '--cleaners',
            type=int,
            help=f"Number of cleaners [Default: {NUMBER_OF_CLEANER_WORKERS}]",
            default=NUMBER_OF_CLEANER_WORKERS
        )
        parser.add_argument(
            '--fruits',
            type=int,
            help=f"Number of fruits in the tree at the beginning [Default: {INITIAL_NUMBER_OF_FRUITS}]",
            default=INITIAL_NUMBER_OF_FRUITS
        )
        parser.add_argument("--verbose", help="increase output verbosity",
                            action="store_true")
        return parser


@unique
class ParserVersion(Enum):
    """
    An enumeration of the different parser versions
    """

    v1: argparse.ArgumentParser = Parser.get_v1()

    @classmethod
    def _missing_(cls, value):
        """
        Assumes v1 as the default parser
        :param value: not used
        :return:
        """
        return cls.v1


class Cli:
    """
    A class used to represent the Command Line Interface
    """

    def __init__(self, parser_version: ParserVersion = ParserVersion.v1):
        """

        :param parser_version: version of the CLI argument parser
        """
        self.parser = parser_version.value

    def parse(self, args=None):
        """
        Receives the list of arguments inserted via CLI, interprets if and return the parsed arguments
        :param:
        :return:
        """

        if args is None:
            args = sys.argv[1:]

        parsed_vars = self.parser.parse_args(args)

        if hasattr(parsed_vars, "verbose") and parsed_vars.verbose:
            os.environ["DEBUG"] = "True"

        return parsed_vars
