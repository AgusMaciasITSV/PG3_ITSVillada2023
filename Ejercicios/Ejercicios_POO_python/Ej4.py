class Operacion:#Se define la clase Operacion
    def __init__ (self, a, b):
        self.a = a
        self.b = b
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        print(f"{self.a} más {self.b} es igual a: {self.a + self.b}")
    
    def resta(self):
        print(f"{self.a} menos {self.b} es igual a: {self.a - self.b}")

    def multiplicacion(self):
        print(f"{self.a} multiplicado por {self.b} es igual a: {self.a * self.b}")

    def division(self):
        if self.b == 0:
            print("No se puede dividir por 0")
        else:
            print(f"{self.a} dividido {self.b} es igual a: {self.a / self.b}")

#Se inicializan 2 objetos tipo Operacion
print("\nOperacion 1:\n")
op1 = Operacion(3,4)
print("\n")

print("Operacion 2:\n")
op2 = Operacion(5,0)
print("\n")