from queue import Queue


class ModifiedQueue(Queue):
    """
    A class that represents a modified queue
    """

    name = "Undefined State"
    unit = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.executing_tasks = 0

    def __str__(self):
        """
        String representation
        :return:
        """
        unit_separator = " " if self.unit else ""
        return f"{self.name} ({self.unfinished_tasks - self.executing_tasks}{unit_separator}{self.unit})"
