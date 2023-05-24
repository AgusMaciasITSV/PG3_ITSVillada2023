import unittest
from ej5 import search_matrix
class test5(unittest.TestCase):
    def setUp(self) -> None:
        self.search = search_matrix()
    def test_search_matrix(self):
        resultado = self.search.search_matrix([1,3,5,7,9],1)
        self.assertEqual(resultado,True)

        resultado1 = self.search.search_matrix([113,333,451,552],10)
        self.assertEqual(resultado1,False)