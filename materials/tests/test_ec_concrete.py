import unittest
from materials.concretes.ec_concrete import EcConcrete

class Test_EcConcrete(unittest.TestCase):

    def test_class_constructor(self):

        with self.assertRaises(ValueError):
            EcConcrete(name='WRONG', fck=-20, density=2400)
            EcConcrete(name='WRONG', fck=25, density=-2400)

        EcConcrete(name='WRONG', fck=25, density=2400)