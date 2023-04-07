class Familia: #Se define la clase Familia y sus metodos
    def __init__(self, padre, madre, listaHijos):
        self.padre = padre
        self.madre = madre
        self.listaHijos = listaHijos

    def __str__(self):
        hijos_str = ", ".join(self.listaHijos)
        return f"Padre: {self.padre}\nMadre: {self.madre}\nHijos: {hijos_str}"

#Se crea un objeto tipo Familia y se printean sus datos mediante el método __str__
familia = Familia("Tomás","Delfina",["Juan","Maxi","Micaela"])
print(familia)