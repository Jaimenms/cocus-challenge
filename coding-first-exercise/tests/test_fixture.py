import os
from unittest import TestCase
from tests.fixtures.case1 import Case1Fixture


class TestFixture(TestCase):

    def setUp(self):
        self.case1 = Case1Fixture()

    def test_read_fixture(self):
        self.assertTrue(self.case1.inputs, list)

    def test_create_tree_from_fixture(self):
        self.case1.create_tree()
        self.assertTrue(os.path.exists(self.case1.root))

    def tearDown(self):
        self.case1.remove_tree()
