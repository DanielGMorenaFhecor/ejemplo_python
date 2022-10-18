from abc import abstractmethod
from materials.material import Material

class Concrete(Material):
    """Base class for all concrete materials"""

    def __init__(self, name: str, density=2400.0):
        """
        Initializes a new instance of a concrete material

        Parameters
        ----------
        name : str
            name of the concrete material
        density : float
            concrete density in kg/m3 (default is 2400.0kg/m3)

        Raises
        ------
        ValueError
            if densify is less than zero
        """

        super().__init__(name,density)

    @property
    @abstractmethod
    def fck(self) -> float:
        """Returns the concrete compressive strength in MPa"""


    @property
    @abstractmethod
    def Ecm(self) -> float:
        """Returns the concrete modulus of elasticity in MPa"""