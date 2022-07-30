

class SuffixException(Exception):
    def __init__(self, s, *args):
        super().__init__(args)
        self.s = s


class EmptySuffixException(SuffixException):

    def __str__(self):
        return f"The suffix \"{self.s}\" cannot be empty"


class InvalidSuffixException(SuffixException):

    def __str__(self):
        return f"The suffix \"{self.s}\" is not valid"


class AmbiguousSuffixException(SuffixException):

    def __str__(self):
        return f"It is not possible to identify if \"{self.s}\" is a suffix or a prefix"
