import os

from .exceptions import path_exceptions
from .files import Files
from .predicate import Predicate


class Folder:
    """
    A class that represents a folder
    """

    def __init__(self, path: str):
        """

        :param path: A string with the path of the folder
        """
        self.validate(path=path)
        self.path = path

    @staticmethod
    def validate(path: str):
        """
        The path string is validated according to the following rules:
            - It cannot be empty;
            - It cannot have asterisks

        :param path: A string with the path of the folder
        :return:
        """
        if not path:
            raise path_exceptions.EmptyPathException(path)

        if path.find("*") >= 0:
            raise path_exceptions.InvalidPathException(path)

        if not os.path.exists(path):
            raise path_exceptions.NotFoundPathException(path)

        if not os.path.isdir(path):
            raise path_exceptions.NotAPathException(path)

    def traverse(self, predicate: Predicate) -> Files:
        """
        A method that traverses a directory tree with root corresponding to the corrent folder
        :param predicate: object that represent a predicate that assumes multiple filtering criteria
        :return:
        """
        files = Files(files=[], root=self.path)
        for dirname, _, filenames in self.traverse_step():
            files += Files.create(root=self.path, dirname=dirname, filenames=filenames, predicate=predicate)
        return files

    def traverse_step(self):
        return os.walk(self.path)
