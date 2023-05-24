import unittest
from ej1 import validate_password
class test1(unittest.TestCase):
    def setUp(self) -> None:
        self.validate = validate_password()
    def test_validate_password(self):
        resultado = self.validate.validate_password("Pepe123")
        self.assertEqual(resultado,False)

        resultado1 = self.validate.validate_password("Messi2024!")
        self.assertEqual(resultado1,True)