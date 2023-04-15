class Alumno: #Se define la clase Alumno
    nombre = ""
    nota = 0

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setNota(self, nota):
        self.nota = nota

    def getNombre(self):
        return self.nombre
    
    def getNota(self):
        return self.nota
    
    def estaAprobado(self): #Debido a que la consigna en el documento esta incompleta, se reemplazo por un metodo para saber si un alumno aprobó
        if self.nota >= 6:
            return "El alumno "+self.nombre+" está aprobado."
        else:
            return "El alumno "+self.nombre+" no está aprobado."

#Se crean ambas clases y se llama el metodo estaAprobado()

almn1 = Alumno()
almn1.setNombre("Maxi")
almn1.setNota(9)
print(almn1.estaAprobado())

almn2 = Alumno()
almn2.setNombre("Mateo")
almn2.setNota(3)
print(almn2.estaAprobado())