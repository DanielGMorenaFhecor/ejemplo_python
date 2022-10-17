import unittest
from structural_standards.concrete.eurocode import Eurocode_1992_2

class TestEurocodeConcrete(unittest.TestCase):
    
    def setUp(self) -> None:
        self.eurocode = Eurocode_1992_2()

    def tearDown(self) -> None:
        pass

    def test_beta_cc(self):
        self.assertEqual(self.eurocode.beta_cc(t=28,s=0.35), 1)


if __name__ == '__main__':
    unittest.main()