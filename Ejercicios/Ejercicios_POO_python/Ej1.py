#Se designa la clase Persona asi como sus metodos

class Persona:
    nombre = ""

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

#Se crea el objeto persona1, se le asigna nombre y se muestra en pantalla
persona1 = Persona()

persona1.setNombre("Lucas")
print(persona1.getNombre())

#Se crea el objeto persona1, se le asigna nombre y se muestra en pantalla
persona2 = Persona()

persona2.setNombre("Martin")
print(persona2.getNombre())


