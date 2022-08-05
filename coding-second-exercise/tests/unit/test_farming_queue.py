from unittest import TestCase
from app.queues.farming_queue import FarmingQueue
from app.exceptions.queue_exceptions import QueueException


class TestFarmingQueue(TestCase):


    def test_worker_validate(self):

        f = FarmingQueue()
        f.validate()

    def test_worker_not_valid(self):

        f = FarmingQueue()
        f.executing_tasks = 1

        with self.assertRaises(QueueException) as _:
            f.validate()
