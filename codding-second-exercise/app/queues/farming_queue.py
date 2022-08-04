from queue import Queue
from ..exceptions import queue_exceptions


class FarmingQueue(Queue):
    """
    A class that represents a modified queue
    """

    name = "Farming Queue"
    unit = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.executing_tasks = 0

    def validate(self):
        """
        Method to validate the initial condition of the queue
        :return:
        """

        if self.executing_tasks != 0:
            raise queue_exceptions.QueueIsUnderExecutionException(self.name)

    @property
    def quantity(self):
        """
        Method that calculate the number of tokens in the queue (excluding poisoning ones)
        :return:
        """
        return len([value for value in self.queue if value is not None])

    def __str__(self):
        """
        String representation
        :return:
        """
        unit_separator = " " if self.unit else ""
        return f"{self.name} ({self.quantity}{unit_separator}{self.unit})"
