import unittest
from materials.concretes.aci_concrete import AciConcrete

class Test_Aci_318_19_Concrete(unittest.TestCase):

    def test_class_constructor(self):

        with self.assertRaises(ValueError):
            AciConcrete(name='WRONG', fc=-10, wc=2400)
            AciConcrete(name='WRONG', fc=25, wc=-1000)

        AciConcrete(name='RIGHT', fc=25, wc=2400)