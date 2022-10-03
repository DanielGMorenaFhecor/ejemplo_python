#LA CLASE PRINCIPAL de la AASHTO
from structural_standards.structural_standard import StructuralStandard

class Aashto(StructuralStandard):

    def __init__(self):
        super().__init__(name='AASHTO')

    def Ec(self, density: float, fc: float) -> float:
        return density**1.5 * 0.043 * fc**0.5
