from abc import ABC, abstractmethod
from materials.concretes.concrete import Concrete

class ConcreteFactory(ABC):
    """Abstract base class for concrete factory"""

    @abstractmethod
    def create_concrete(self) -> Concrete:
        """Instantiates a new Concrete material Instance"""