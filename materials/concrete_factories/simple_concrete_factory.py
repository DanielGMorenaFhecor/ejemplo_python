from materials.concretes.concrete import Concrete
from materials.concrete_factories.concrete_factory import ConcreteFactory
from materials.concretes.ec_concrete import EcConcrete
from materials.concretes.aci_concrete import AciConcrete

class SimpleConcreteFactory(ConcreteFactory):
    """Simple example for a concrete factory design pattern"""

    @staticmethod
    def __get_valid_norm_names():
        return ('ec', 'aci')

    def __init__(self, norm_name: str, fck: float):
        """
        Creates an instance of SimpleConcreteFactory

        Parameters
        ----------
        norm_name : str
            specify one of the following: 'ec' for EUROCODE or 'aci' for ACI Standard
        fck : float
            concrete compressive strength in MPa

        Raises
        ------
        ValueError
            if not valid norm name
        ValueError
            if resistance is less than 0
        """

        norm_name=norm_name.lower()
        if norm_name not in SimpleConcreteFactory.__get_valid_norm_names():
            raise ValueError(f'Specified norm name is not valid. Current: {norm_name}')
        if fck < 0:
            raise ValueError(f'Concrete compression strength cannot be less than zero. Current {fck}')

        self._norm_name = norm_name
        self._fck = fck

    def create_concrete(self) -> Concrete:
        """Creates an instance of a Concrete Base Class"""
        
        if self._norm_name=='ec':
            return EcConcrete(f'C{int(self._fck)}', fck=self._fck)
        if self._norm_name=='aci':
            return AciConcrete(f'C{int(self._fck)}', fc=self._fck)
        
        raise ValueError(f'Norm name {self._norm_name} is not valid')