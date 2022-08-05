import os
import sys
from threading import Timer, Thread, Event
from typing import List

from ..exceptions import machine_exceptions
from ..logger import get_logger
from ..queues.farming_queue import FarmingQueue
from ..tools import list_to_string, calculate_token
from ..workers.worker import Worker


class Machine:
    """
    A class that represents the machine. This machine is composed by queues and workers. A set of workers with the same
    purpose is responsible to process elements from one queue to the consecutive queue.
    """

    def __init__(self, from_queue: FarmingQueue, name: str = "machine", log_interval: float = None):
        """

        :param name: machine name
        :param from_queue: initial queue of the machine
        :param log_interval: time interval in seconds between each log display
        """

        logger = get_logger(__name__)

        self.name = name

        self.workers = []

        # Initiating a list of queues
        self.queues = [from_queue]

        # Reading lov interval
        log_interval = float(os.getenv("LOG_INTERVAL", 1.0)) if log_interval is None else log_interval
        logger.debug("Log will be printed every {log_interval} seconds.")

        # Instantiating the timer for the log thread
        self.timer = Machine.MachineTimer(log_interval, self.log)

        self.logger = logger

        # Total number of tasks (or tokens) to be processed
        self.number_of_jobs = 0

    def validate(self):
        """
        Method that validates if the machine is valid
        :return:
        """

        # Validating the machine itself
        if self.get_first_queue().unfinished_tasks == 0:
            raise machine_exceptions.MachineWithNothingToProcessException(self.name)

        # Validating workers
        for worker in self.workers:
            worker.validate()

        # Validating queues
        for queue in self.queues:
            queue.validate()

    def workers_are_stoped(self):
        """
        Methos that checks if all workers are stoped
        :return:
        """
        for key, value in self.measure_workers().items():
            if value != 0:
                return False
        return True

    def queues_at_final_state(self):
        """
        Method that checks if the queues are at the final state
        :return:
        """

        last_key = self.get_last_queue().name

        for key, value in self.measure_queues().items():
            if key == last_key and value != self.number_of_jobs:
                return False
            elif key != last_key and value != 0:
                return False

        return True


    def add_workers(self, workers: List[Worker], to_queue: FarmingQueue):
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
            self.logger.debug(f"Adding worker {worker} to get work from {from_queue} to {to_queue}")

        # Appending the to_queue to the queue list
        self.queues.append(to_queue)
        self.logger.debug(f"Adding queue {to_queue} to the machine chain")

        return self

    def get_first_queue(self) -> FarmingQueue:
        """
        A method to get the first queue
        :return:
        """
        return self.queues[0]

    def get_last_queue(self) -> FarmingQueue:
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
        self.number_of_jobs = number_of_jobs

        for _ in range(number_of_jobs):
            self.get_first_queue().put(calculate_token())
        return self

    def log(self):
        """
        A simple log method
        :return:
        """
        self.logger.info(self)

    def execute(self):
        """
        A method to execute the machine
        :return:
        """

        self.start()
        self.wait()
        self.stop()

    def start(self):
        """
        A method to start the machine
        :return:
        """
        self.log()
        self.timer.start()
        for worker in self.workers:
            self.logger.debug(f"Starting worker {worker}")
            worker.thread.start()

    def wait(self):
        """
        A method to wait for the conclusion of the machine jobs
        :return:
        """
        for queue in self.queues:

            if queue != self.get_last_queue():
                self.logger.debug(f"Waiting for the conclusion of queue {queue}")
                queue.join()

            self.logger.debug(f"Deallocating workers with queue {queue} as upstream")
            self.poisoning(queue)
            self.logger.debug(f"Deallocation concluded of {queue}")

    def poisoning(self, q):
        """
        A method to apply the poisoning approach to conclude a thread send a job with None value
        :param q: object represented a queue that with receive a poison
        :return:
        """

        # For every worker that have q as upstream queue
        for worker in self.workers:
            if worker.from_queue == q:
                self.logger.debug(f"Deallocating worker {worker} from queue {q}")
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

    class MachineTimer(Timer):
        """
        A class to create a repeat timer in the Machine
        """

        def __init__(self, interval, function, args=None, kwargs=None):
            Thread.__init__(self)
            self.interval = interval
            self.function = function
            self.args = args if args is not None else []
            self.kwargs = kwargs if kwargs is not None else {}
            self.finished = Event()

        def run(self):
            while not self.finished.wait(self.interval):
                self.function(*self.args, **self.kwargs)

    def measure_workers(self):
        """

        :return:
        """
        return {worker.fullname: worker.quantity for worker in self.workers}

    def measure_queues(self):
        """

        :return:
        """
        return {queue.name: queue.quantity for queue in self.queues}

    def __str__(self):
        """
        Representing the machine as a string
        :return:
        """

        queues_str = list_to_string(self.queues)
        workers_str = list_to_string(self.workers)
        return f"{queues_str} - {workers_str}"

