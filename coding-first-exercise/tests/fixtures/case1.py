from . import Fixture


class Case1Fixture(Fixture):
    """
    A class that represents a fixture with the example case of the codding challenge
    """

    suffix = "*.log"

    inputs = [
        ("./a", None),
        ("./a", "bbb"),
        ("./a", "bbb.log"),
        ("./a/ddd", None),
        ("./", "aaa.log"),
        ("./", "abc.txt"),
    ]

    outputs = [
        "./aaa.log",
        "./a/bbb.log"
    ]
