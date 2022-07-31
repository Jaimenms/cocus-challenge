from .worker import Worker


class PickerWorker(Worker):

    name = "farmer"
    MIN_DURATION = 3
    MAX_DURATION = 6
