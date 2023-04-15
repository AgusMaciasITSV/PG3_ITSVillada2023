while True:
    try:
        meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        i = int(input("Ingrese el numero de mes: "))
        if i != 0 and 0 < i:
            print(f"El numero de mes {i} es: {meses[i-1]}")
            x = input("¿Desea continuar? Ingrese si para continuar, o cualquier otra cosa para cancelar: ")
            if x == "si":
                pass
            else:
                break
        else:
            print("El numero ingresado esta fuera de rango\n")
    except ValueError:
        print("El numero ingresado no es valido o no esta expresado de forma decimal")
    except IndexError:
        print("El numero ingresado esta fuera de rango\n")