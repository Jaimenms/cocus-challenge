class MachineException(Exception):
    def __init__(self, name, *args):
        super().__init__(args)
        self.name = name


class MachineWithNothingToProcessException(MachineException):

    def __str__(self):
        return f"The machine \"{self.name}\" does not have what to process"
