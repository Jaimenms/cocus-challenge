from .operator import Operator
from ..workers.cleaner import CleanerWorker


class ClearOperator(Operator):

    def __init__(self, from_queue, to_queue, quantity: int = 1):

        workers = [CleanerWorker(identifier=identifier) for identifier in range(1, quantity + 1)]

        super().__init__(workers, from_queue, to_queue)
