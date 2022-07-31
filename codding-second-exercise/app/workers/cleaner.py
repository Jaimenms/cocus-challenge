from .worker import Worker


class CleanerWorker(Worker):

    name = "cleaner"
    MIN_DURATION = 2
    MAX_DURATION = 4
