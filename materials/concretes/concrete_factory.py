from materials.concretes.aashto_concrete import AashtoConcrete
from materials.concretes.concrete import Concrete
from materials.concretes.ec_concrete import EcConcrete

# Esta clase únicamente se dedica a crear instancias de las diferentes clases de hormigón
class ConcreteFactory():

    def create_concrete(self, norm_name: str,  strength: float) -> Concrete:
        if norm_name.lower()=='ec':
            return EcConcrete(f'C{int(strength)}', fck=strength)
        elif norm_name.lower()=='aashto':
            return AashtoConcrete(f'C{int(strength)}', fc=strength)
        else:
            raise ValueError(f'No existe la norma: {norm_name}')