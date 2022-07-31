from app.operators.operator import Operator
from app.workers.picker import PickerWorker


class PickOperator(Operator):

    def __init__(self, from_queue, to_queue, quantity: int = 1):

        workers = [PickerWorker(identifier=identifier) for identifier in range(quantity)]

        super().__init__(workers, from_queue, to_queue)
