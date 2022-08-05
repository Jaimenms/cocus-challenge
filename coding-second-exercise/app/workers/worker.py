import os
from abc import ABC, abstractmethod
from threading import Thread

from ..exceptions import worker_exceptions
from ..logger import get_logger
from ..queues.farming_queue import FarmingQueue


class Worker(ABC):
    """
    A class that represents the worker
    """

    name = "undefined"
    MIN_DURATION = os.getenv("MIN_DURATION", default=1)
    MAX_DURATION = os.getenv("MAX_DURATION", default=1)

    def __init__(self, identifier: int = 0):
        """

        :param identifier: a integer that identifies the worker
        """

        logger = get_logger(name=f"{self.name}{identifier}")
        logger.debug(f"Instantiating {self.name} with id {identifier}")

        self.identifier = identifier
        self.quantity = 0
        self.thread = None
        self.from_queue = None
        self.to_queue = None
        self.logger = logger

    @property
    def fullname(self):
        """
        Full name of the worker
        :return:
        """
        return self.name+str(self.identifier)

    def validate(self):
        """
        Method that validates if the worker is correctly configured
        :return:
        """

        if self.from_queue is None:
            raise worker_exceptions.WorkerUpstreamQueueNotAssignedException(self.name)

        if self.from_queue is None:
            raise worker_exceptions.WorkerDownstreamQueueNotAssignedException(self.name)

        if self.from_queue == self.to_queue:
            raise worker_exceptions.WorkerCyclicConfigurationException(self.name)

    def pre_task(self, token):
        """
        A method that to all the necessary steps before the worker executes the task
        :param token: task identifier
        :return:
        """

        self.logger.debug(f"Worker {self.name} with id {self.identifier} started pre-task phase on token {token}")

        # Incrementing the number of tokens been executed by this worker
        self.quantity += 1

        # Incrementing the number of tokens collected from the upstream queue to be executed
        self.from_queue.executing_tasks += 1

        self.logger.debug(f"Worker {self.name} with id {self.identifier} concluded pre-task phase on token {token}")

    def post_task(self, token):
        """
        A method that to all the necessary steps after the worker executes the task
        :param token: task identifier
        :return:
        """

        self.logger.debug(f"Worker {self.name} with id {self.identifier} started post-task phase on token {token}")

        # Transfering token to the downstream queue
        self.to_queue.put(token)

        # Decrementing the number of jobs in execution
        self.quantity -= 1
        self.from_queue.executing_tasks -= 1

        self.from_queue.task_done()

        self.logger.debug(f"Worker {self.name} with id {self.identifier} concluded post-task phase on token {token}")

    def run(self):
        """
        A method to run the worker
        :return:
        """

        while True:

            # Getting a job from upstream
            token = self.from_queue.get(block=True)

            # Checking for poisoning
            if token is None:
                self.from_queue.task_done()
                break

            # Execution sequence
            self.pre_task(token)
            self.task(token)
            self.post_task(token)


    def set_thread(self, from_queue: FarmingQueue, to_queue: FarmingQueue):
        """
        A method that prepare the worker for multithreading
        :param from_queue: the upstream queue
        :param to_queue: the downstream queue
        :return:
        """

        self.from_queue = from_queue
        self.to_queue = to_queue
        self.thread = Thread(target=self.run, args=())

    @abstractmethod
    def task(self, job):
        """
        A method that corresponds to the task
        :param job: job identifier
        :return:
        """
        pass

    def __str__(self):
        """
        String representation
        :return:
        """
        return f"{self.name}{self.identifier} ({self.quantity})"
