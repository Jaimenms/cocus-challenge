import os


class File:
    """
    A class used to represent a file
    """

    def __init__(self, dirname: str, filename: str):
        """

        :param dirname: directory name of the file
        :param filename: filename of the file
        """
        self.filename = filename
        self.filepath = os.path.join(dirname, filename)

    def relpath(self, start="."):
        """
        This method presents the relative path of the file in relation to the start path
        :param start: a start path
        :return:
        """
        return "./" + os.path.relpath(self.filepath, start=start)
