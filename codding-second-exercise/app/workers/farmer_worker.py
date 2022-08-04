import os
from random import uniform
from time import sleep

from .worker import Worker


class FarmerWorker(Worker):

    name = "farmer"
    DEFAULT_MIN_DURATION = 1.0
    DEFAULT_MAX_DURATION = 1.0

    def __init__(self, identifier: int = 0, min_duration: float = DEFAULT_MIN_DURATION,
                 max_duration: float = DEFAULT_MAX_DURATION,
                 fast_forward_factor: float = None):
        """

        :param identifier: integer to identify a cleaner farmer
        :param min_duration: minimum duration of the simulated job in seconds
        :param max_duration: maximum duration of the simulated job in seconds
        :param fast_forward_factor: this factor is used to get faster results for a simulation (for testing purpose)
        """
        super().__init__(identifier=identifier)
        self.min_duration = min_duration
        self.max_duration = max_duration

        self.fast_forward_factor = float(
            os.getenv("FAST_FORWARD_FACTOR", "1.0")) if fast_forward_factor is None else fast_forward_factor

    def task(self, token):
        """
        A method that simulates the time spends in the execution of the task
        :param token: task identifier
        :return:
        """

        self.logger.debug(f"Worker {self.name} with id {self.identifier} started working on token {token}")

        duration = uniform(self.min_duration, self.max_duration) / self.fast_forward_factor

        self.logger.debug(f"Worker {self.name} with id {self.identifier} will be working for {duration:.3f} s")
        sleep(duration)

        self.logger.debug(f"Worker {self.name} with id {self.identifier} concluded his work on token {token}")
