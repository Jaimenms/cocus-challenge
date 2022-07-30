from unittest import TestCase
from app.criterias.suffix import Suffix
from app.exceptions import suffix_exceptions as exceptions


class TestSuffix(TestCase):

    def test_validate_suffix_string_valid(self):
        """
        Test if it does not raises an exception with a valid string
        :return:
        """

        suffix_string = "*.log"
        Suffix.validate(criteria_value=suffix_string)

    def test_validate_suffix_string_empty(self):
        """
        Test if the empty strings raises a EmptySuffixException during validation
        :return:
        """

        suffix_string = ""
        with self.assertRaises(exceptions.EmptySuffixException) as _:
            Suffix.validate(criteria_value=suffix_string)

    def test_validate_suffix_string_without_initial_star(self):
        """
        Test if a string that does not start with star raises a InvalidSuffixException during validation
        :return:
        """

        suffix_string = ".log"
        with self.assertRaises(exceptions.InvalidSuffixException) as _:
            Suffix.validate(criteria_value=suffix_string)

    def test_validate_suffix_string_ambiguous(self):
        """
        Test if a string with double star raises a Ambiguous during validation
        :return:
        """

        suffix_string = "*.log*"
        with self.assertRaises(exceptions.AmbiguousSuffixException) as _:
            Suffix.validate(criteria_value=suffix_string)

    def test_valid_constructor(self):
        """
        Test if constructor can construct object
        :return:
        """

        Suffix(criteria_value="*.log")
        self.assertTrue(True)

    def test_invalid_constructor(self):
        """
        Test if constructor can construct object
        :return:
        """

        with self.assertRaises(exceptions.SuffixException) as _:
            Suffix(criteria_value=".log")
