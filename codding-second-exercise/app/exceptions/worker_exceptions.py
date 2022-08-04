class WorkerException(Exception):
    def __init__(self, name, *args):
        super().__init__(args)
        self.name = name


class WorkerUpstreamQueueNotAssignedException(WorkerException):

    def __str__(self):
        return f"The upstream queue of worker \"{self.name}\" was not defined"


class WorkerDownstreamQueueNotAssignedException(WorkerException):

    def __str__(self):
        return f"The downstream queue of worker \"{self.name}\" was not defined"


class WorkerCyclicConfigurationException(WorkerException):

    def __str__(self):
        return f"The worker \"{self.name}\" cannot have equal upstream and dowstream queue"
