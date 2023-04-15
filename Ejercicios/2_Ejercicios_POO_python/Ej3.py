class Triangulo: #Se crea la clase Triangulo y sus metodos
    lado1 = 0
    lado2 = 0
    lado3 = 0

    def setLado1(self, lado):
        self.lado1 = lado

    def setLado2(self, lado):
        self.lado2 = lado

    def setLado3(self, lado):
        self.lado3 = lado

    def getLado1(self):
        return self.lado1
    
    def getLado2(self):
        return self.lado2
    
    def getLado3(self):
        return self.lado3
    
    def ladoMayor(self):
        if self.lado1 >= self.lado2:
            if self.lado1 >= self.lado3:
                return self.lado1
            else:
                return self.lado3
        else:
            if self.lado2 >= self.lado3:
                return self.lado2
            else:
                return self.lado3
            
    def esEquilatero(self):
        if self.lado1 == self.lado2 & self.lado1 == self.lado3:
            return "Si, es un triangulo equilatero"
        else:
            return "No, no es un triangulo equilatero"
        
#Se instancian 2 objetos

trg1 = Triangulo()
trg1.setLado1(3)
trg1.setLado2(4)
trg1.setLado3(5)

print("El lado mayor es: "+str(trg1.ladoMayor()))
print(trg1.esEquilatero())

print("\n")

trg2 = Triangulo()
trg2.setLado1(3)
trg2.setLado2(3)
trg2.setLado3(3)

print("El lado mayor es: "+str(trg2.ladoMayor()))
print(trg2.esEquilatero())