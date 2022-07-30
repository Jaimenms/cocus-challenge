from abc import ABC, abstractmethod

from ..file import File


class Criteria(ABC):

    def __init__(self, criteria_value: str):
        """
        String with the value of the filename suffix
        :param criteria_value:
        """
        self.validate(criteria_value)

    @property
    @abstractmethod
    def value(self):
        pass

    @staticmethod
    @abstractmethod
    def validate(criteria_value: str):
        """
        The suffix string is validated according to the following rules:
            - It cannot be empty;
            - It must start with an asterisk
            - It can only have one asterisk

        :param criteria_value:
        :return:
        """
        pass

    @abstractmethod
    def matches(self, file: File) -> bool:
        """
        Checks if the file with name equal to filename has this suffix
        :param filename: name of the file
        :return:
        """
        return True
