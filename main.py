from materials.concretes.aashto_concrete import AashtoConcrete
from materials.concretes.concrete_factory import ConcreteFactory
from materials.concretes.ec_concrete import EcConcrete

# El objetivo del programa es demostrar que, independientemente de cómo definamos la forma de crear un hormigón, 
# o sus parámetros iniciales o del constructor, desde fuera podamos acceder a sus propiedades físicas intrínsecas 
# que pertenecen a cualquier tipo de hormigón (Módulo elástico, resistencia,...)

print('--INICIO DEL PROGRAMA--')
print('-----------------------')

print('--HORMIGÓN EUROCÓDIGO--')
ec_concrete=EcConcrete('C30',fck=30)
print(f'Ecm={ec_concrete.Ecm()} MPa') # Implementación concreta para HORMIGÓN EUROCÓDIGO
print(f'Módulo elástico={ec_concrete.Ecm()} MPa') # Implementación genérica para TODOS los hormigones
print(f'fck={ec_concrete.fck} MPa') # Implementación concreta para HORMIGÓN EUROCÓDIGO
print(f'Resistencia={ec_concrete.fck()} MPa') # Implementación genérica para TODOS los hormigones
print('---------------------')

print('--HORMIGÓN AASHTO--')
aashto_concrete=AashtoConcrete('C30',fc=30)
print(f'Ec={aashto_concrete.Ec()} MPa') # Implementación concreta para HORMIGÓN AASHTO
print(f'Módulo elástico={aashto_concrete.Ecm()} MPa') # Implementación genérica para TODOS los hormigones
print(f'fc={aashto_concrete.fc} MPa') # Implementación concreta para HORMIGÓN AASHTO
print(f'Resistencia={aashto_concrete.fck()} MPa') # Implementación genérica para TODOS los hormigones
print('---------------------')

# La clase CONCRETE FACTORY nos permite crear hormigones independientemente de sus parámetros para definirlos
print('Selecciona el tipo de hormigón:') # Preguntamos al usuario si quiere un hormigón del EC o de la AASHTO
concrete_type = input('[EC] o [AASHTO]: ')

# Creamos una instancia de la clase que únicamente se dedica a generar hormigones de diferentes normativas con sus parámetros respectivos
strength=(float)(input('Inserta valor para la resistencia [MPa]: '))
concrete_factory = ConcreteFactory()
concrete = concrete_factory.create_concrete(concrete_type, strength)

print('--HORMIGÓN DEFNIDO POR EL USUARIO--')
print(f'Módulo elástico={concrete.Ecm()} MPa') # Implementación genérica para TODOS los hormigones
print(f'Resistencia={concrete.fck()} MPa') # Implementación genérica para TODOS los hormigones
print('---------------------')

print('--FIN DEL PROGRAMA--')