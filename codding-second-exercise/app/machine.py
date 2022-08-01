from typing import List

from .tools import RepeatTimer, list_to_string, calculate_token
from .queues.modified_queue import ModifiedQueue
from .workers.worker import Worker
from .setup import logger


class Machine:
    """
    A class that represents the machile. This machine is composed by queues and workers. A set of workers with the same
    purpose is responsible to process elements from one queue to the consecutive queue.
    """

    def __init__(self, from_queue: ModifiedQueue, log_interval: float = 1.0):
        """

        :param from_queue: initial queue of the machine
        :param log_interval: time interval in seconds between each log display
        """

        self.workers = []

        # Initiating a list of queues
        self.queues = [from_queue]

        # Instantiating the timer for the log thread
        self.timer = RepeatTimer(log_interval, self.log)


    def add_workers(self, workers: List[Worker], to_queue: ModifiedQueue):
        """
        This method get a list of workers and append this to the machine workers list and also identify the queue where
        the worker will get the job (from_queue) and the queue that the job will be delivered (to_queu)
        :param workers: a list of worker objects
        :param to_queue: the object that represent the queue where the job will be delivered to.
        :return:
        """

        # As this machine consists of a chaim of queues, the from_queue for the workers corresponds to the last queue
        # stored in the queue list.
        from_queue = self.get_last_queue()

        # Setting the thread of each worker added to the machine
        for worker in workers:
            worker.set_thread(from_queue, to_queue)
            self.workers.append(worker)

        # Appending the to_queue to the queue list
        self.queues.append(to_queue)

        return self

    def get_first_queue(self) -> ModifiedQueue:
        """
        A method to get the first queue
        :return:
        """
        return self.queues[0]

    def get_last_queue(self) -> ModifiedQueue:
        """
        A method to get the last queue
        :return:
        """
        return self.queues[-1]

    def feed_first_queue(self, number_of_jobs: int):
        """
        A method to feed the first queue with new jobs
        :param number_of_jobs: Number of jobs to be fed
        :return:
        """
        for _ in range(number_of_jobs):
            self.get_first_queue().put(calculate_token())
        return self

    def log(self):
        """
        A simple log method
        :return:
        """
        logger.info(self)

    def start(self):
        """
        A method to start the machine
        :return:
        """
        self.log()
        self.timer.start()
        for worker in self.workers:
            worker.thread.start()

    def wait(self):
        """
        A method to wait for the conclusion of the machine jobs
        :return:
        """
        for q in self.queues:
            if q != self.get_last_queue():
                q.join()
            self.poisoning(q)

    def poisoning(self, q):
        """
        A method to apply the poisoning approach to conclude a thread send a job with None value
        :param q: object represented a queue that with receive a poison
        :return:
        """

        # For every worker that have q as upstream queue
        for worker in self.workers:
            if worker.from_queue == q:
                q.put(None)

    def stop(self):
        """
        A method to to all necessary steps to stop the machine
        :return:
        """

        # Cancel the timer
        self.timer.cancel()

        # Add a final log to guarantee that all necessary information is displayed
        self.log()


    def __str__(self):
        """
        Representing the machine as a string
        :return:
        """

        queues_str = list_to_string(self.queues)
        workers_str = list_to_string(self.workers)
        return f"{queues_str} - {workers_str}"
