from typing import List
from .file import File
from .exceptions import files_exceptions as exceptions
from .predicate import Predicate


class Files:

    def __init__(self, files: List[File], root: str):
        """
        A class used to represent a collection of files
        :param files: list of files
        :param root: path root used to represent relative path of each file
        """
        self.root = root
        self.content = files

    @staticmethod
    def create(root: str, dirname: str, filenames: list, predicate: Predicate):
        """
        A method that create Files based a list of filenames contained in dirname, a reference root directory and
        a predicate.
        :param root: path root used to represent relative path of each file
        :param dirname: directory of the files
        :param filenames: list with the files
        :param predicate: predicate with a collection of filtering criterias
        :return:
        """
        files = []
        for filename in filenames:
            file = File(dirname, filename)
            if predicate.matches(file=file):
                files.append(file)
        return Files(files=files, root=root)

    def __add__(self, other):
        """

        :param other: Files objected to be cummed (or combined)
        :return:
        """

        # Raising an error if the Files have diferrent root folders
        if other.root != self.root:
            raise exceptions.FilesCombinationException(self.root, other.root)

        return Files(files=self.content + other.content, root=self.root)

    def list_relpath(self) -> list:
        """
        List the relative path of files using root as the start folder
        :return:
        """
        return [file.relpath(start=self.root) for file in self.content]

    def __str__(self):
        """
        String representation of the list of files
        :return:
        """
        return "\n".join(self.list_relpath())

