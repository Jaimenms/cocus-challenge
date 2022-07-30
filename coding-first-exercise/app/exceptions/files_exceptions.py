

class FilesCombinationException(Exception):

    def __init__(self, a, b, *args):
        super().__init__(args)
        self.a = a
        self.b = b

    def __str__(self):
        return f"The files with root {self.a} cannot be combined with other with root {self.b}"
