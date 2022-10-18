from materials.concretes.concrete import Concrete
from structural_standards.concrete.aci import Aci_318_19

class AciConcrete(Concrete):
    """ACI Standard Concrete Material Class"""

    def __init__(self, name: str, fc: float, wc=2286.04):
        """
        Inicializes a new instance of ACI Standard concrete material

        Parameters
        ----------
        name : str
            name of the concrete material
        fc : float
            value of the concrete compressive strength fc' in MPa according to ACI 318-19 19.2.1
        wc : float
            concrete density in kg/m3
            
        Raises
        ------
        ValueError
            if compressive strength fc is less than zero
        ValueError
            if density wc is less than zero
        """

        if fc < 0:
            raise ValueError(f"Compressive strength fc' cannot be less than zero. Current: {fc}")

        super().__init__(name, density=wc)
        self._fc = fc
        self._aci = Aci_318_19()

    def Ecm(self) -> float:
        """
        ACI 318-19 19.2.2
        Returns the concrete modulus of elasticity in MPa
        """
        return self.Ec()

    def Ec(self) -> float:
        """
        ACI 318-19 19.2.2
        Returns the concrete modulus of elasticity in MPa
        """
        return self._aci.Ec(self._fc, wc=self.density)

    def fck(self) -> float:
        """
        ACI 318-19 19.2.1
        Returns the concrete compressive strength fc' in MPa
        """
        return self.fc

    @property
    def fc(self) -> float:
        """
        ACI 318-19 19.2.1
        Returns the concrete compressive strength fc' in MPa
        """
        return self.fc
