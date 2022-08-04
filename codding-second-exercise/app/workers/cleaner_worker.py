from .farmer_worker import FarmerWorker


class CleanerWorker(FarmerWorker):
    name = "cleaner"
    DEFAULT_MIN_DURATION = 2.0
    DEFAULT_MAX_DURATION = 4.0

    def __init__(self, identifier: int = 0, min_duration: float = DEFAULT_MIN_DURATION,
                 max_duration: float = DEFAULT_MAX_DURATION):
        """

        :param identifier: integer to identify a cleaner farmer
        :param min_duration: minimum duration of the simulated job in seconds
        :param max_duration: maximum duration of the simulated job in seconds
        """
        super().__init__(identifier=identifier, min_duration=min_duration, max_duration=max_duration)
