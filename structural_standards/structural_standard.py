from abc import ABC

class StructuralStandard(ABC):

    def __init__(self, name: str):
        self.name=name