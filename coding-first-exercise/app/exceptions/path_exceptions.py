

class PathException(Exception):
    def __init__(self, p, *args):
        super().__init__(args)
        self.p = p


class EmptyPathException(PathException):

    def __str__(self):
        return f"The path \"{self.p}\" cannot be empty"


class InvalidPathException(PathException):

    def __str__(self):
        return f"The path \"{self.p}\" cannot contain an asterisk"


class NotFoundPathException(PathException):

    def __str__(self):
        return f"The path \"{self.p}\" was not found in the filesystem"

class NotAPathException(PathException):

    def __str__(self):
        return f"The string \"{self.p}\" does not point to a path"
