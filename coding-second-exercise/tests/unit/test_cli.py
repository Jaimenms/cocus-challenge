from unittest import TestCase
from app.cli import Cli, ParserVersion
from argparse import ArgumentParser


class TestCli(TestCase):

    def test_get_parser(self):
        parser_version = ParserVersion.v1
        self.assertIsInstance(parser_version.value, ArgumentParser)

    def test_parse_ok(self):
        args = []
        Cli().parse(args)
        self.assertTrue(True)
