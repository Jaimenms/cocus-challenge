import argparse
import sys
from enum import Enum, unique


class Parser:
    """
    A class used to encapsulate all the methods of the CLI parser in different versions
    """

    @staticmethod
    def get_v1() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description="List of paths and file names that match a certain suffix")
        parser.add_argument('suffix', type=str, help="Suffix of the file name to be found. Example: *.log")
        parser.add_argument('path', type=str, help="Path of the file system. Example: /var/tmp")
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

        return self.parser.parse_args(args)
