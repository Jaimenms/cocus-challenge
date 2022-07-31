from time import sleep
from random import random
from app.queues.fruit_queue import FruitQueue
import logging

FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format=FORMAT)

class Worker:

    name = "undefined"
    MIN_DURATION = .1
    MAX_DURATION = 1

    def __init__(self,identifier: int = 0):
        self.identifier = identifier
        self.quantity = 0

    def run(self, from_queue: FruitQueue, to_queue: FruitQueue):
        while True:
            job = from_queue.get(block=True)
            if job is None:
                break
            self.quantity += 1
            t = (self.MAX_DURATION - self.MIN_DURATION) * random() + self.MIN_DURATION
            from_queue.task_done()
            sleep(t)
            to_queue.put(job)
            self.quantity -= 1
        from_queue.task_done()

    def __str__(self):
        return f"{self.name}{self.identifier} ({self.quantity})"

