# La clase CONCRETE es hija de la clase MATERIAL
from materials.material import Material
from abc import abstractmethod

class Concrete(Material):

    def __init__(self, name: str):

        # Invoco al constructor padre y le paso el nombre
        super().__init__(name,density=2400) # Density=2400kg/m3

    @abstractmethod
    def Ecm(self) -> float:
        pass

    @abstractmethod
    def fck(self) -> float:
        pass