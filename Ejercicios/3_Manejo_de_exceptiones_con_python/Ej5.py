while True:
    try:
        x = int(input("\nIngrese: \n 1 si desea guardar texto\n 2 si desea leer texto \n 3 si desea salir\n\n"))
        if x == 1:
            text = input("\nIngrese el texto que desea almacenar:\n")
            f = open("TextoAlmacenado.txt", "w")
            f.write(text)
            f.close()
        elif x == 2:
            f = open("TextoAlmacenado.txt", "r")
            print("="*50)
            print(f.read())
            f.close()
            print("="*50)
        elif x == 3:
            break
        else:
            print("Ingrese una opcion valida\n")
    except ValueError:
        print("Ingrese un numero valido y en formato decimal.\n")
    except FileNotFoundError:
        print("No se encuentra ningun archivo, porfavor cree uno.")
