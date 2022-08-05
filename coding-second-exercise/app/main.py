from .cli import Cli, ParserVersion
from .machines.farming_machine import FarmingMachine


def main():

    # Console API
    args = Cli(parser_version=ParserVersion.v1).parse()

    # Instantiating Machine
    machine = FarmingMachine(
        number_of_pickers=args.pickers,
        number_of_cleaners=args.cleaners,
        number_of_fruits=args.fruits
    )

    # Validate Machine
    machine.validate()

    # Executing Machine
    machine.execute()


if __name__ == "__main__":

    main()
