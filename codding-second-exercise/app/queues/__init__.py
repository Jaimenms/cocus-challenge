"""Queue package"""

from .at_tree import AtTreeQueue
from .clean import CleanQueue
from .dirty import DirtyQueue

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
