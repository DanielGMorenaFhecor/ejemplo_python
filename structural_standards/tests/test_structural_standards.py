import unittest
from structural_standards.structural_standard import StructuralStandard

class TestStructuralStandard(unittest.TestCase):

    def setUp(self) -> None:
        self.standard = StructuralStandard(name='test_std', release_year=2022)

    def tearDown(self) -> None:
        pass

    def test_nothing(self):
        pass

if __name__ == '__main__':
    unittest.main()