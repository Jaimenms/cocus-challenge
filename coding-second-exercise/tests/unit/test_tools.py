from unittest import TestCase
from app.tools import list_to_string, calculate_token


class Test(TestCase):
    def test_list_to_string(self):
        """
        Testing list_to_string with default separator
        :return:
        """

        cases = [
            ([], ''),
            (['a', 'b'], 'a - b'),
            (['a', 1], 'a - 1'),
        ]

        for i, (_input, expected) in enumerate(cases):
            with self.subTest(i=i):
                calculated = list_to_string(_input)
                self.assertEqual(calculated, expected)

    def test_list_to_string_different_separator(self):
        """
        Testing list_to_string with custom separator
        :return:
        """

        separator = "|"

        cases = [
            ([], ''),
            (['a', 'b'], 'a|b'),
            (['a', 1], 'a|1'),
        ]

        for i, (_input, expected) in enumerate(cases):
            with self.subTest(i=i):
                calculated = list_to_string(_input, separator=separator)
                self.assertEqual(calculated, expected)

    def test_calculate_token_length(self):
        """
        Testing length of token
        :return:
        """
        calculated = calculate_token()
        self.assertEqual(len(calculated), 6)

    def test_calculate_token_difference(self):
        """
        Testing if subsequent tokens are different
        :return:
        """
        calculated_1 = calculate_token()
        calculated_2 = calculate_token()
        self.assertNotEqual(calculated_1, calculated_2)

