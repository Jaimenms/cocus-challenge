class QueueException(Exception):
    def __init__(self, name, *args):
        super().__init__(args)
        self.name = name


class QueueIsUnderExecutionException(QueueException):

    def __str__(self):
        return f"The upstream queue of worker \"{self.name}\" was not defined"