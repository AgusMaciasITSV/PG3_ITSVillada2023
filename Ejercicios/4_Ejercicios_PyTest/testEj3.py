import unittest
from ej3 import verificarAnagrama
class test3(unittest.TestCase):
    def setUp(self) -> None:
        self.anagrama = verificarAnagrama()
    def test_verificarAnagrama(self):
        resultado = self.anagrama.verificarAnagrama("Hola,Halo")
        self.assertEqual(resultado,True)

        resultado1 = self.anagrama.verificarAnagrama("queso,esque")
        self.assertEqual(resultado1,False)