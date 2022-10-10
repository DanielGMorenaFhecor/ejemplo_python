from materials.concretes.concrete import Concrete
from structural_standards.aashto.aashto import Aashto

# La clase AASHTO CONCRETE es hija de CONCRETE
class AashtoConcrete(Concrete):

    def __init__(self, name: str, fc: float):
        super().__init__(name)
        self.fc = fc
        self.aashto = Aashto()

    def Ecm(self) -> float:
        return self.Ec()

    def Ec(self) -> float:
        return self.aashto.Ec(self.density, self.fc)

    def fck(self) -> float:
        return self.fc