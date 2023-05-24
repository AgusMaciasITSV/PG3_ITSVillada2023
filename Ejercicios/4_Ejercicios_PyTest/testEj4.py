import unittest
from ej4 import calculate_statistics
class test4(unittest.TestCase):
    def setUp(self) -> None:
        self.statistic = calculate_statistics()
    def test_calculate_statistics(self):
        resultado = self.statistic.calculate_statistics([2,2,2,2])
        self.assertEqual(resultado,f"Media: {2}\nDesviación Estándar: {0}")

        resultado1 = self.statistic.calculate_statistics([5,6,7,8,9])
        self.assertEqual(resultado1,f"Media: {7}\nDesviación Estándar: {1.5811388300841898}")