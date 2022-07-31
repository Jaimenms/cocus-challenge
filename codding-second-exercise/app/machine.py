import os
import uuid
import logging

from typing import List
from threading import Timer, Thread

from app.workers.worker import Worker
from app.queues.fruit_queue import FruitQueue

LOGS_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(filename=os.path.join(LOGS_FOLDER, 'logfile.log'), level=logging.DEBUG, format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


class Machine:

    def __init__(self, from_queue: FruitQueue):
        self.queues = [from_queue]
        self.threads = []
        self.workers = []

    def add(self, workers: List[Worker], to_queue: FruitQueue):
        for worker in workers:
            from_queue = self.queues[-1]
            t = Thread(target=worker.run, args=(from_queue, to_queue))
            self.threads.append(t)
            self.queues.append(to_queue)
        self.workers += workers
        return self

    def feed(self, n: int):
        for _ in range(n):
            item = uuid.uuid4().hex
            self.queues[0].put(item)
        return self

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
