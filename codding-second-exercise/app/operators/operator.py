from typing import List
from ..workers.worker import Worker
from app.queues.fruit_queue import FruitQueue


class Operator:

    def __init__(self, workers: List[Worker], from_queue: FruitQueue, to_queue: FruitQueue):
        self.workers = workers
        self.from_queue = from_queue
        self.to_queue = to_queue
