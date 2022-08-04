import time
from unittest import TestCase
from app.workers.farmer_worker import FarmerWorker
from app.exceptions.worker_exceptions import WorkerException


class TestFarmerWorker(TestCase):

    def test_worker_is_valid(self):

        class FarmingQueue:
            pass

        q1 = FarmingQueue()
        q2 = FarmingQueue()

        f = FarmerWorker()
        f.set_thread(from_queue=q1, to_queue=q2)
        f.validate()

    def test_worker_not_valid(self):

        with self.assertRaises(WorkerException) as _:
            FarmerWorker().validate()

    def test_task(self):

        duration = 0.1
        n = 10
        f = FarmerWorker(identifier=0, min_duration=duration, max_duration=duration)

        t1 = time.time()
        for _ in range(n):
            f.task("any")
        t2 = time.time()
        simulated_duration = t2-t1
        expected_duration = n * duration
        self.assertAlmostEqual(simulated_duration, expected_duration, places=1)
