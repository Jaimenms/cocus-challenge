from .at_tree import AtTreeQueue
from .clean import CleanQueue
from .dirty import DirtyQueue


_QUEUES = {
    'at_tree': AtTreeQueue,
    'dirty': DirtyQueue,
    'clean': CleanQueue,
}


def create_queue(name, *args, **kwargs):
    return _QUEUES[name](*args, **kwargs)
