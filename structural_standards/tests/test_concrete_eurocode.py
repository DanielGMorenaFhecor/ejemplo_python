import unittest
from structural_standards.concrete.eurocode import Eurocode_1992_2

class Test_Eurocode_1992_2(unittest.TestCase):
    
    def setUp(self) -> None:
        self.eurocode = Eurocode_1992_2()

    def tearDown(self) -> None:
        pass

    def test_national_annex_instance(self):

        with self.assertRaises(ValueError):
            Eurocode_1992_2(national_code='WRONG')

        Eurocode_1992_2(national_code='ES')

    def test_beta_cc(self):
        
        with self.assertRaises(ValueError):
            self.eurocode.beta_cc(t=-123, s=-0.3)
            self.eurocode.beta_cc(t=24,s=1.4)

        self.assertEqual(self.eurocode.beta_cc(t=28,s=0.35), 1)
        self.assertEqual(self.eurocode.beta_cc(t=14,s=0.35), 0.8650441379410829)
        self.assertEqual(self.eurocode.beta_cc(t=5,s=0.20), 0.7608748550686041)