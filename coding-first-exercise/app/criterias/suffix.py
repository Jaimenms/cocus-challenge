from ..exceptions import suffix_exceptions
from ..file import File
from .criteria import Criteria


class Suffix(Criteria):

    def __init__(self, criteria_value: str):
        """
        String with the value of the filename suffix
        :param criteria_value:
        """
        super().__init__(criteria_value)
        self._value = criteria_value[1:]

    @property
    def value(self):
        return self._value

    @staticmethod
    def validate(criteria_value: str):
        """
        The suffix string is validated according to the following rules:
            - It cannot be empty;
            - It must start with an asterisk
            - It can only have one asterisk

        :param criteria_value:
        :return:
        """
        if not criteria_value:
            raise suffix_exceptions.EmptySuffixException(criteria_value)

        if not criteria_value.startswith("*"):
            raise suffix_exceptions.InvalidSuffixException(criteria_value)

        if criteria_value[1:].find("*") >= 0:
            raise suffix_exceptions.AmbiguousSuffixException(criteria_value)

    def matches(self, file: File) -> bool:
        """
        Checks if the file with name equal to filename has this suffix
        :param filename: name of the file
        :return:
        """
        return file.filename.endswith(self._value)
