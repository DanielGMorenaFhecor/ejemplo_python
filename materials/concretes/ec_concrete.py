from materials.concretes.concrete import Concrete
from structural_standards.eurocodes.eurocode import Eurocode

# La clase EUROCODE CONCRETE es hija de CONCRETE
class EcConcrete(Concrete):
    
    # Podemos tener parámetros en el constructor de ECCONCRETE adicionales a los de CONCRETE
    def __init__(self, name: str, fck):
        super().__init__(name)
        self.eurocode = Eurocode()
        self.fck = fck

    def elastic_mod(self) -> float:
        return self.Ecm()

    def Ecm(self):
        return self.eurocode.Ecm(self.fck)

    def strength(self) -> float:
        return self.fck

    