print("Ingrese un año:")
while True:
    try:
        x = int(input())
    except:
        print("Ingrese una opcion valida")
    else:
        if (x % 400 == 0) and (x % 100 == 0):
            print("El año "+str(x)+" es bisiesto.")
        elif (x % 4 ==0) and (x % 100 != 0):
            print("El año "+str(x)+" es bisiesto.")
        else:
            print("El año "+str(x)+" no es bisiesto.")