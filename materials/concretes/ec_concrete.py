from materials.concretes.concrete import Concrete
from structural_standards.concrete.eurocode import Eurocode_1992_2

class EcConcrete(Concrete):
    """EN 1992-2 Concrete Material Class"""

    def __init__(self, name: str, fck: float, density=2400.0, national_code=''):
        """
        Initializes a new instance of a EN 1992-2 Concrete

        Parameters
        ----------
        name : str
            name of the concrete
        fck : float
            concrete compressive strength MPa according to EN 1992-1.2:2004 3.1.2
        density : float
            concrete density in kg/m3
        national_code : str
            country code if any national annex required (default is '')

        Raises
        ------
        ValueError
            if density is less than zero (default is 2400kg/m3)
        ValueError
            if compressive strength fck is less than zero
        ValueError
            if national_code does not exist
        """
        
        if density < 0:
            raise ValueError(f'Density cannot be less than zero. Current {density}')
        if fck < 0:
            raise ValueError(f'Compressive strength fck cannot be less than zero. Current {fck}')

        super().__init__(name, density=density)
        self._eurocode = Eurocode_1992_2(national_code=national_code)
        self._fck = fck

    def Ecm(self):
        """
        EN 1992-1.2:2004 Table 3.1
        Returns the concrete modulus of elasticity at 28 days in MPa
        """
        return self._eurocode.Ecm(self.fck)

    def fck(self) -> float:
        """
        EN 1992-1.2:2004 3.1.2
        Returns the concrete compressive strength at 28 days in MPa
        """
        return self._fck

    