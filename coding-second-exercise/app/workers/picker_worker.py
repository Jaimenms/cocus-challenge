from .farmer_worker import FarmerWorker


class PickerWorker(FarmerWorker):

    DEFAULT_MIN_DURATION = 3.0
    DEFAULT_MAX_DURATION = 6.0

    def __init__(self, identifier: int = 0, min_duration: float = DEFAULT_MIN_DURATION,
                 max_duration: float = DEFAULT_MAX_DURATION):
        """

        :param identifier: integer to identify a picker farmer
        :param min_duration: minimum duration of the simulated job in seconds
        :param max_duration: maximum duration of the simulated job in seconds
        """
        super().__init__(identifier=identifier, min_duration=min_duration, max_duration=max_duration)
