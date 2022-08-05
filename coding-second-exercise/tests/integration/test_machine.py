from unittest import TestCase
from app.machines.machine import Machine
from app.queues.farming_queue import FarmingQueue
from app.workers.farmer_worker import FarmerWorker



class IntegrationTestMachine(TestCase):

    def execution_test(self, m: Machine):
        m.execute()
        self.assertTrue(m.workers_are_stoped())
        self.assertTrue(m.queues_at_final_state())


    def test_machine_one_worker_two_queues(self):
        """
        Big bang testing considering one worker and two queries
        :return:
        """

        w = FarmerWorker(max_duration=0.001, min_duration=0.001)
        q1 = FarmingQueue()
        q2 = FarmingQueue()
        n = 2
        m = Machine(from_queue=q1).add_workers(workers=[w], to_queue=q2).feed_first_queue(number_of_jobs=n)
        m.validate()
        self.execution_test(m)


    def test_machine_two_workers_two_queues(self):
        """
        Big bang testing considering tww workers and two queries
        :return:
        """

        w1 = FarmerWorker(max_duration=0.001, min_duration=0.001)
        w2 = FarmerWorker(max_duration=0.001, min_duration=0.001)
        q1 = FarmingQueue()
        q2 = FarmingQueue()
        m = Machine(from_queue=q1).add_workers(workers=[w1, w2], to_queue=q2).feed_first_queue(2)
        m.validate()
        m.execute()

    def test_machine_two_workers_three_queues(self):
        """
        Big bang testing considering two workers and three queries
        :return:
        """

        w1 = FarmerWorker(max_duration=0.001, min_duration=0.001)
        w2 = FarmerWorker(max_duration=0.001, min_duration=0.001)
        q1 = FarmingQueue()
        q2 = FarmingQueue()
        q3 = FarmingQueue()
        m = Machine(from_queue=q1).\
            add_workers(workers=[w1], to_queue=q2).\
            add_workers(workers=[w2], to_queue=q3).\
            feed_first_queue(2)
        m.validate()
        self.execution_test(m)

    def test_machine_many_workers_in_two_queries(self):
        """
        Big bang testing considering many workers and two queries
        :return:
        """

        workers = [FarmerWorker(max_duration=0.001, min_duration=0.001) for _ in range(100)]
        q1 = FarmingQueue()
        q2 = FarmingQueue()
        m = Machine(from_queue=q1)\
            .add_workers(workers=workers, to_queue=q2)\
            .feed_first_queue(2)
        m.validate()
        self.execution_test(m)

    def test_machine_many_workers_many_queries(self):
        """
        Big bang testing considering many workers and two queries
        :return:
        """

        q0 = FarmingQueue()
        m = Machine(from_queue=q0)

        for _ in range(100):
            w = FarmerWorker(max_duration=0.001, min_duration=0.001)
            q = FarmingQueue()
            m.add_workers(workers=[w], to_queue=q)
        m.feed_first_queue(2)
        m.validate()
        self.execution_test(m)
