from abc import ABC

class StructuralStandard(ABC):
    """
    Parent class that compresss all general data regarding to any Structural Standard Code

    Attributes
    name : str
        name of the current structural code
    release_year : int
        the year the structural code was released
    ---------
    """

    def __init__(self, name: str, release_year: int):
        """
        Parameters
        ----------
        name : str
            The name of the Structural Standard Code
        release_year : int
            The year the Structural Code was released
        """

        self.name=name
        self.release_year=release_year
