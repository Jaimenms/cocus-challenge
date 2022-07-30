from typing import List
from .criterias.criteria import Criteria
from .file import File


class Predicate:

    def __init__(self, criterias: List[Criteria]):
        self.criterias = criterias

    def matches(self, file: File):
        for criteria in self.criterias:
            if not criteria.matches(file):
                return False
        return True
