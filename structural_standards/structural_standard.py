from abc import ABC

class StructuralStandard(ABC):
    """
    Parent class that compresss all general data regarding to any Structural Standard Code

    Attributes
    name : str
        name of the current structural code
    release_year : int
        the year the structural code was released
    materials : tuple
        tuple with application materials for the current standard
    ---------
    """
   
    def __init__(self, name: str, release_year: int, materials: tuple):
        """
        Parameters
        ----------
        name : str
            The name of the Structural Standard Code
        release_year : int
            The year the Structural Code was released
        materials : tuple
            Tuple with strings that cover each one of the application materials for this standard
        """

        self._name=name
        self._release_year=release_year
        self._materials=materials

    @property
    def name(self) -> str:
        """Returns the name of the structural standard"""
        return self._name

    @property
    def release_year(self) -> int:
        """Returns the release year of the structural standard"""
        return self._release_year

    @property
    def materials(self) -> tuple:
        """Return the materials covered by this standard"""
        return self._materials

