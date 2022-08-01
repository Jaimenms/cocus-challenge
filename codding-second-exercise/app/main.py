import sys
from .cli import Cli, ParserVersion
from .machine import Machine
from .queues import create_queue
from .workers import create_worker

# Parameters
LOG_INTERVAL = 1 # seconds


def main():

    args = Cli(parser_version=ParserVersion.v1).parse(sys.argv[1:])

    # Creating workers
    picker_workers = [
        create_worker(name="picker", identifier=identifier) for identifier in range(args.pickers)
    ]
    cleaner_workers = [
        create_worker(name="cleaner", identifier=identifier) for identifier in range(args.cleaners)
    ]

    # Creating Queues
    at_tree = create_queue(name="at_tree")
    dirty = create_queue(name="dirty")
    clean = create_queue(name="clean")

    # Creating Machine
    machine = Machine(from_queue=at_tree, log_interval=LOG_INTERVAL)\
        .add_workers(picker_workers, to_queue=dirty)\
        .add_workers(cleaner_workers, to_queue=clean)\
        .feed_first_queue(args.fruits)

    # Executing Machine
    machine.start()
    machine.wait()
    machine.stop()


if __name__ == "__main__":

    main()
