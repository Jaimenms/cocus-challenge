from unittest import TestCase
from unittest.mock import MagicMock
from app.machines.machine import Machine

class TestMachine(TestCase):

    def setUp(self):
        class FarmingQueue:
            pass

        q1 = FarmingQueue()
        q1.unfinished_tasks = 10
        q1.validate = MagicMock(return_value=True)
        q1.put = MagicMock(return_value=True)
        self.q1 = q1

        q2 = FarmingQueue()
        q2.unfinished_tasks = 10
        q2.validate = MagicMock(return_value=True)
        self.q2 = q2

        class CleanerWorker:
            pass
        w = CleanerWorker()
        w.validate = MagicMock(return_value=True)
        w.set_thread = MagicMock(return_value=True)
        self.w = w

    def test_validate(self):
        m = Machine(from_queue=self.q1)
        m.validate()

    def test_add_workers(self):
        m = Machine(from_queue=self.q1)
        m.add_workers(workers=[self.w], to_queue=self.q2)

    def test_feed_first_queue(self):
        m = Machine(from_queue=self.q1)
        m.feed_first_queue(1)
        m.validate()
