import os
from unittest import TestCase, mock
from app.machines.farming_machine import FarmingMachine


class TestFarmingMachine(TestCase):

    def execution_test(self, m: FarmingMachine):
        m.execute()
        self.assertTrue(m.workers_are_stoped())
        self.assertTrue(m.queues_at_final_state())

    @mock.patch.dict(os.environ, {"FAST_FORWARD_FACTOR": "200.0"})
    def test_farming_machine(self):
        """
        Big bang testing considering many workers and two queries
        :return:
        """

        m = FarmingMachine(number_of_fruits=10)
        m.validate()
        self.execution_test(m)
