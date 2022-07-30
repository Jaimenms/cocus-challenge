from app.exceptions import path_exceptions as exceptions
import tempfile
from unittest import TestCase
from app.criterias.suffix import Suffix
from app.folder import Folder
from tests.fixtures.case1 import Case1Fixture
from app.predicate import Predicate


class TestFolder(TestCase):

    def setUp(self):
        self.case1 = Case1Fixture()
        self.case1.create_tree()
        self.f1 = Folder(path=self.case1.root)

    def test_traverse(self):
        p1 = Predicate(criterias=[Suffix(criteria_value="*.log"), ])
        files = self.f1.traverse(predicate=p1)
        self.assertEqual(files.list_relpath(), self.case1.outputs)

    def test_validate_path_string_valid(self):
        """
        Test if it does not raises an exception with a valid string
        :return:
        """

        path_string = "/var/log"
        Folder.validate(path=path_string)

    def test_validate_path_string_empty(self):
        """
        Test if the empty strings raises a EmptyPathException during validation
        :return:
        """

        path_string = ""
        with self.assertRaises(exceptions.EmptyPathException) as _:
            Folder.validate(path=path_string)

    def test_validate_path_string_that_does_not_exist(self):
        """
        Test if a string that does not start with star raises a InvalidPathException during validation
        :return:
        """

        path_string = "/this_folder_does_not_exist"
        with self.assertRaises(exceptions.NotFoundPathException) as _:
            Folder.validate(path=path_string)

    def test_validate_path_string_with_star(self):
        """
        Test if a string that does not start with star raises a InvalidPathException during validation
        :return:
        """

        path_string = "/var/log/*"
        with self.assertRaises(exceptions.InvalidPathException) as _:
            Folder.validate(path=path_string)

    def test_valid_constructor(self):
        """
        Test if constructor can construct object
        :return:
        """

        path_string = tempfile.gettempdir()
        Folder(path=path_string)
        self.assertTrue(True)

    def test_invalid_constructor(self):
        """
        Test if constructor can construct object
        :return:
        """

        with self.assertRaises(exceptions.PathException) as _:
            Folder(path="/this_folder_does_not_exist")
