while True:
    try:
        a = int(input("Ingrese su primer numero: "))
        b = int(input("Ingrese su segundo numero: "))
        print(f"La suma de los valores ingresados es: {a+b}\n")
        x = input("¿Desea seguir sumando? Ingrese si para continuar, o cualquier otra cosa para cancelar: ")
        if x == "si":
            pass
        else:
            break

    except ValueError:
        print("El numero ingresado debe ser expresado en numeros decimales")
