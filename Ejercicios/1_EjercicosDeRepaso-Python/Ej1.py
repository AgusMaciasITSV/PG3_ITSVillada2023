list = [3,34,5,1,5,8,23]
print("Elija el numero del cual desea saber su indice de la siguiente lista:")
print(list)
while True:
    try:
        x = int(input())
    except:
        print("Por favor, ingrese un caracter valido.")
    else:
        if x in list:
            print("El indice del numero ingresado es: "+str(list.index(x)))
            break
        else:
            print("El numero ingresado no se encuentra dentro de la lista.")