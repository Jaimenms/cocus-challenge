from app.exceptions import files_exceptions as exceptions
from unittest import TestCase
from tests.fixtures.case1 import Case1Fixture
from app.files import Files
from app.file import File


class TestFiles(TestCase):

    def setUp(self):
        self.case1 = Case1Fixture()
        self.case1.create_tree()
        self.file_objs_1 = [File(dirname, filename) for dirname, filename in self.case1.inputs if filename is not None]

    def test_init(self):
        Files(files=self.file_objs_1, root=self.case1.root)
        self.assertTrue(True)

    def test_sum(self):
        a = Files(files=self.file_objs_1, root=self.case1.root)
        b = Files(files=self.file_objs_1, root=self.case1.root)
        c = a + b
        self.assertTrue(True)

    def test_sum_with_different_root(self):
        a = Files(files=self.file_objs_1, root=self.case1.root)
        b = Files(files=self.file_objs_1, root="other")
        with self.assertRaises(exceptions.FilesCombinationException) as _:
            c = a + b
        self.assertTrue(True)

    def test_str(self):
        a = Files(files=self.file_objs_1, root=self.case1.root)
        self.assertIsInstance(str(a),str)
