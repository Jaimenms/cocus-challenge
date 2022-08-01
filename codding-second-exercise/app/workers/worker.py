from time import sleep
from random import random
from threading import Thread
from ..queues.modified_queue import ModifiedQueue


class Worker:
    """
    A class that represents the worker
    """

    name = "undefined"
    MIN_DURATION = 1
    MAX_DURATION = 1

    def __init__(self, identifier: int = 0):
        """

        :param identifier: a integer that identifies the worker
        """
        self.identifier = identifier
        self.quantity = 0
        self.thread = None
        self.from_queue = None
        self.to_queue = None

    def pre_job(self, job):
        """
        A method that to all the necessary steps before the worker executes the job
        :param job: job identifier
        :return:
        """
        # Incrementing the number of jobs in execution
        self.quantity += 1
        self.from_queue.executing_tasks += 1

    def run_job(self, job):
        """
        A method that simulates the time spends in the execution of the job
        :param job: job identifier
        :return:
        """
        sleep((self.MAX_DURATION - self.MIN_DURATION) * random() + self.MIN_DURATION)

    def post_job(self, job):
        """
        A method that to all the necessary steps after the worker executes the job
        :param job: job identifier
        :return:
        """

        # Transfering the job to the downstream queue
        self.to_queue.put(job)

        # Decrementing the number of jobs in execution
        self.quantity -= 1
        self.from_queue.executing_tasks -= 1

        self.from_queue.task_done()

    def run(self):
        """
        A method to run the worker
        :return:
        """

        # Start Looping
        while True:

            # Getting a job from upstream
            job = self.from_queue.get(block=True)

            # Checking for poisoning
            if job is None:
                self.from_queue.task_done()
                break

            # Execution sequence
            self.pre_job(job)
            self.run_job(job)
            self.post_job(job)


    def set_thread(self, from_queue: ModifiedQueue, to_queue: ModifiedQueue):
        """
        A method that prepare the worker for multithreading
        :param from_queue: the upstream queue
        :param to_queue: the downstream queue
        :return:
        """

        self.from_queue = from_queue
        self.to_queue = to_queue
        self.thread = Thread(target=self.run, args=())

    def __str__(self):
        """
        String representation
        :return:
        """
        return f"{self.name}{self.identifier} ({self.quantity})"

