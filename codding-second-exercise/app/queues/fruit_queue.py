from queue import Queue

class FruitQueue(Queue):

    name = "Undefined State"
    unit = ""

    def __str__(self):
        return f"{self.name} ({self.unfinished_tasks} {self.unit})"
