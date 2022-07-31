from .machine import Machine
from .queues import create_queue
from .workers import create_worker


def main():

    # Creating workers
    picker_workers = [create_worker(name="picker", identifier=identifier) for identifier in range(3)]
    cleaner_workers = [create_worker(name="cleaner", identifier=identifier) for identifier in range(2)]

    # Creating Queues
    at_tree = create_queue(name="at_tree")
    dirty = create_queue(name="dirty")
    clean = create_queue(name="clean")

    # Creating Machine
    machine = Machine(from_queue=at_tree) \
        .add(picker_workers, to_queue=dirty)\
        .add(cleaner_workers, to_queue=clean)\
        .feed(50)

    machine.run()


if __name__ == "__main__":

    main()
