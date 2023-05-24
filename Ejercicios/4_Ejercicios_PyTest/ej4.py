def calculate_statistics(lista):
    suma = 0
    for x in lista:
        suma = suma+x
    media = suma/len(lista)

    m = 0
    for i in lista:
        m = m+(i-media)**2
    desviacionEstandar = (m/(len(lista)-1))**(1/2)

    print(f"Media: {media}\nDesviación Estándar: {desviacionEstandar}")

lista = [1,2,3,4,5] # Lista de numeros a la cual se le aplicaran las operaciones
calculate_statistics(lista)