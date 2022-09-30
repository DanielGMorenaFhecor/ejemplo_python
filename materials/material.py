from abc import ABC, abstractproperty

# La clase PADRE de todos los Materiales
class Material(ABC):

    # Únicamente (de momento) va a tener una propiedad de nombre
    def __init__(self, name: str, density: float):
        self.name = name
        self.density=density