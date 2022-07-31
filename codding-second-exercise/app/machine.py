import uuid
import logging

from typing import List
from threading import Timer, Thread
import threading

from .operators.operator import Operator

FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")



class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

class Machine:

    def __init__(self, operators: List[Operator]):
        self.queues = []
        self.threads = []
        self.workers = []
        for operator in operators:
            self.add_operator(operator)
            self.queues.append(operator.from_queue)
            self.workers += operator.workers
        self.queues.append(operators[-1].to_queue)

        self.initial_queue = operators[0].from_queue
        self.final_queue = operators[-1].to_queue

    def add_operator(self, operator: Operator):
        for worker in operator.workers:
            t = Thread(target=worker.run, args=(operator.from_queue, operator.to_queue))
            self.threads.append(t)

    def feed(self, n: int):
        for _ in range(n):
            item = uuid.uuid4().hex
            self.initial_queue.put(item)

    def log(self):
        logging.info(self)

    def run(self):
        self.log()

        timer = RepeatTimer(1.0, self.log)
        timer.start()

        for t in self.threads:
            t.start()

        for q in self.queues[0:-1]:
            q.join()

        for q in self.queues:
            for _ in range(len(self.workers)):
                q.put(None)

        timer.cancel()
        self.log()


    def __str__(self):
        queues_ctt = [str(queue) for queue in self.queues]
        workers_ctt = [str(worker) for worker in self.workers]
        queues_str = " - ".join(queues_ctt)
        workers_str = " - ".join(workers_ctt)
        return f"{queues_str} - {workers_str}"
