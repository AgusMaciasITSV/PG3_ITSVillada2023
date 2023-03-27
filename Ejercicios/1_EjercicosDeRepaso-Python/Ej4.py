while True:
    try:
        lst = []
        print("Ahora ingresara 5 numeros que luego seran ordenados de mayor a menor:")
        for x in range(5):
            print("Ingrese su numero")
            a = int(input())
            lst.append(a)
            print("")
        lst.sort(reverse = True)
        print(lst)
        break
    except:
        print("Ingrese un numero valido")
        print("")

