import unittest
from ej2 import romanToDecimal
class test2(unittest.TestCase):
    def setUp(self) -> None:
        self.roman = romanToDecimal()
    def test_romanToDecimal(self):
        resultado = self.roman.romanToDecimal("XXIV")
        self.assertEqual(resultado,24)

        resultado1 = self.roman.romanToDecimal("XL")
        self.assertEqual(resultado1,40)