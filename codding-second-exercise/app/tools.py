from threading import Timer
import uuid


class RepeatTimer(Timer):
    """
    A class to creat a repeat timer
    """
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


def list_to_string(elements: list, separator: str = " - "):
    """
    Converts a list into a string where the elements are separated bu the separator string
    :param elements: a list of elements that can be represented as string
    :param separator: string that will separate the elements
    :return:
    """
    return separator.join([str(element) for element in elements])


def calculate_token(size: int = 6):
    """
    Calculates a token as a unique randon string identifier with a defined size
    :param size: size of the token
    :return:
    """
    return uuid.uuid4().hex[0:size]
