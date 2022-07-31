from .cleaner import CleanerWorker
from .picker import PickerWorker


_WORKERS = {
    'cleaner' : CleanerWorker,
    'picker': PickerWorker,
}


def create_worker(name, *args, **kwargs):
    return _WORKERS[name](*args, **kwargs)
