class Persona: #Se crea la clase Persona y sus metodos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def cargarDatos(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
    
    def imprimirDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
    

class Empleado(Persona): #Se crea la clase Empleado y sus metodos
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
    def cargarDatos(self):
        super().cargarDatos()
        self.sueldo = float(input("Ingrese el sueldo: "))
    
    def imprimirDatos(self):
        super().imprimirDatos()
        print(f"Sueldo: {self.sueldo}")
        
    def debeImpuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos.")
        else:
            print("El empleado no debe pagar impuestos.")

#Se crean las clases y se llaman a los metodos necesarios

pers1 = Persona("",0)
pers1.cargarDatos()
pers1.imprimirDatos()

print("\nEmpleado:\n")
emp1 = Empleado("",0,0)
emp1.cargarDatos()
emp1.debeImpuestos()
print("\n")
emp1.imprimirDatos()