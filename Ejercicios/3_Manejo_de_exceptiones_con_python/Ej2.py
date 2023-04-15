while True:
    try:
        a = int(input("Ingrese su primer numero: "))
        b = int(input("Ingrese su segundo numero: "))
        print(f"La division de los valores ingresados es: {a/b}\n")
        x = input("¿Desea seguir dividiendo? Ingrese si para continuar, o cualquier otra cosa para cancelar: ")
        if x == "si":
            pass
        else:
            break

    except ValueError:
        print("El numero ingresado debe ser expresado en numeros decimales")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
