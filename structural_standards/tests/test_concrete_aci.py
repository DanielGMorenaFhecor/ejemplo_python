import unittest
from structural_standards.concrete.aci import Aci_318_19

class Test_Aci_318_19(unittest.TestCase):

    def setUp(self) -> None:
        self.aci = Aci_318_19()

    def tearDown(self) -> None:
        pass

    def test_Ec(self):

        with self.assertRaises(ValueError):
            self.aci.Ec(fc=-20, wc=2200)
            self.aci.Ec(fc=25, wc=-1000)

        self.assertEqual(self.aci.Ec(fc=21, wc=2286.05), 21538.065351917863)
        self.assertEqual(self.aci.Ec(fc=28, wc=2000), 20351.314453862677)