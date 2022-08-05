"""Workers package"""

from .cleaner_worker import CleanerWorker
from .picker_worker import PickerWorker

# A map to indentify all the available workers
_WORKERS = {
    'cleaner': CleanerWorker,
    'picker': PickerWorker,
}


def create_worker(name, *args, **kwargs):
    """
    A factory method for worker
    :param name: worker name
    :param args:
    :param kwargs:
    :return:
    """
    return _WORKERS[name](*args, **kwargs)
