from materials.concretes.concrete import Concrete

# Esta clase sólo nos va a imprimir info de la clase hormigón
class Printer():

    # Este método sólo imprime la información más intrínseca del hormigón y no se complica 
    # en diferenciar si es EC CONCRETE o AASHTO CONCRETE
    def print_basic_concrete_info(self, concrete: Concrete):
        print()
        print('--CONCRETE INFO--')
        print(f'Name: {concrete.name}')
        print(f'Fcm: {concrete.fcm}')