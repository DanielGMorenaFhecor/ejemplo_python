# La clase CONCRETE es hija de la clase MATERIAL
from materials.material import Material
from abc import abstractmethod

class Concrete(Material):

    def __init__(self, name: str):

        # Invoco al constructor padre y le paso el nombre
        super().__init__(name,density=24.0) # Density=24kN/m3

    @abstractmethod
    def elastic_mod(self) -> float:
        pass

    @abstractmethod
    def strength(self) -> float:
        pass