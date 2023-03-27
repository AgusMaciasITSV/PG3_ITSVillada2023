while True:
    try:
        print("Ingrese el ancho de su rectangulo:")
        x = int(input())
        print("Ingrese el alto de su rectangulo:")
        y = int(input())
        print("Ingrese el caracter a utilizar")
        char = input()

    except:
        print("Ingrese un parametro valido.")
        print("")
    else:
        print("")
        for i in range(y):
            print(char*x)
        print("")
        break 