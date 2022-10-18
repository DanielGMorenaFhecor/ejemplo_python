from abc import ABC

class Material(ABC):
    """Base class for all materials"""

    def __init__(self, name: str, density: float):
        """
        Initializes an instance of a new material
        
        Parameters
        ----------
        name : str
            name of the material
        density : float
            density of the material in kg/m3

        Raises
        ------
        ValueError
            if density is less than z
        """

        if density < 0:
            raise ValueError(f'Density cannot be less than zero. Current {density}')
            
        self._name = name
        self._density=density

    @property
    def name(self):
        """Returns the name of the material"""
        return self._name

    @property
    def density(self):
        """Returns the density of the material in kg/m3"""
        return self._density