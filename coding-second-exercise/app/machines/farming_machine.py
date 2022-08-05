from .machine import Machine
from ..queues import create_queue
from ..workers import create_worker


class FarmingMachine(Machine):
    """
    A class that represents the farming process as a machine. It is composed by a Tree to represent the first queue.
    Then a certain number of picker workers collect the fruit and transfer to the dirty basked queue.
    After that another set of cleaner workers get the fruit from the dirty basket, clean it and transfer to the
    clean basket.
    """

    def __init__(self, number_of_pickers: int = 3, number_of_cleaners: int = 2, number_of_fruits: int = 50):
        """

        :param number_of_pickers: number of picker workers
        :param number_of_cleaners: number of cleaner workers
        :param number_of_fruits: number of fruits at the tree before executing the farming process (machine)
        """

        # Creating Queues
        at_tree = create_queue(name="at_tree")
        dirty = create_queue(name="dirty")
        clean = create_queue(name="clean")

        super().__init__(from_queue=at_tree)

        # Adding Pickers
        picker_workers = [
            create_worker(name="picker", identifier=identifier) for identifier in range(number_of_pickers)
        ]
        self.add_workers(picker_workers, to_queue=dirty)

        # Adding Cleaners
        cleaner_workers = [
            create_worker(name="cleaner", identifier=identifier) for identifier in range(number_of_cleaners)
        ]
        self.add_workers(cleaner_workers, to_queue=clean)

        # Setting number of fruits
        self.feed_first_queue(number_of_fruits)
