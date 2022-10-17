from materials.concretes.concrete import Concrete
from structural_standards.eurocodes.concrete.eurocode import Eurocode_1992_2

# La clase EUROCODE CONCRETE es hija de CONCRETE
class EcConcrete(Concrete):
    
    # Podemos tener parámetros en el constructor de ECCONCRETE adicionales a los de CONCRETE
    def __init__(self, name: str, fck: float):
        super().__init__(name)
        self.eurocode = Eurocode_1992_2()
        self._fck = fck

    def Ecm(self):
        return self.eurocode.Ecm(self.fck)

    def fck(self) -> float:
        return self._fck

    