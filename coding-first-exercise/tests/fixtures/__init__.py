"""Cocus Coding Challenge - first exercise - fxtures"""

import os
import tempfile
import shutil
from pathlib import Path


class Fixture:
    """
    A class to represent a fixture
    """

    # String with the file suffix
    suffix = "*.*"

    # List of tuples with dirname and filename
    inputs = []

    # List of expected output
    outputs = []

    def __init__(self, root=None):
        """

        :param root: root folder (if None a temporary folder is automatically created)
        """

        self.root = root if root is not None else tempfile.mkdtemp()

    def create_tree(self):
        """
        This method creates a directory tree based on the inputs defined in the fixture
        :return:
        """
        for path, filename in self.inputs:
            fullpath = os.path.join(self.root, path)
            if not os.path.exists(fullpath):
                os.makedirs(fullpath, exist_ok=True)
            if filename:
                Path(os.path.join(fullpath, filename)).touch()

    def remove_tree(self):
        """
        This method deleted a directory tree created for this fixture
        :return:
        """
        if self.root is not None:
            shutil.rmtree(self.root)
