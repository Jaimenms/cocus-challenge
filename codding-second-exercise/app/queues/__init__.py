"""Queues package"""

from .tree_queue import AtTreeQueue
from .clean_queue import CleanQueue
from .dirty_queue import DirtyQueue

# A map to indentify all the available queues
_QUEUES = {
    'at_tree': AtTreeQueue,
    'dirty': DirtyQueue,
    'clean': CleanQueue,
}


def create_queue(name, *args, **kwargs):
    """
    A factory method for queue
    :param name: worker name
    :param args:
    :param kwargs:
    :return:
    """
    return _QUEUES[name](*args, **kwargs)
