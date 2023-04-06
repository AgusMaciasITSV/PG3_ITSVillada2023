#Ej1

print("Ejercicio 1")

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

#------------------------------------------------------------------------------

#Ej2

print("Ejercicio 2")

print("Ingrese un año:")
while True:
    try:
        x = int(input())
    except:
        print("Ingrese una opcion valida")
    else:
        if (x % 400 == 0) and (x % 100 == 0):
            print("El año "+str(x)+" es bisiesto.")
		break
        elif (x % 4 ==0) and (x % 100 != 0):
            print("El año "+str(x)+" es bisiesto.")
		break
        else:
            print("El año "+str(x)+" no es bisiesto.")
		break

#-----------------------------------------------------------------------------

#Ej3

print("Ejercico 3")

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


#-----------------------------------------------------------------------------


#Ej4

print("Ejercicio 4")

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

#-----------------------------------------------------------------------------

#Ej5

print("Ejercicio 5")

while True:
    rwrd = ""
    print("Escriba una palabra para averiguar si es un palindromo:")
    wrd = input()
    rwrd = wrd[::-1]
    print(rwrd)
    if wrd == rwrd:
        print("Su palabra SI es un palindromo.")
	break
    else:
        print("Su palabra NO es un palindromo.")
    print("")
	break


#-----------------------------------------------------------------------------

#Ej6

print("Ejercicio 6")

print("Ingrese una palabra:")
w = input()
w = w.upper()
vc = "AEIOU"
i = 0
for x in w:
    for y in vc:
        if x == y:
            i+=1
print("Cantidad de vocales: "+str(i))


#-----------------------------------------------------------------------------

#Ej7

print("Ejercicio 7")

while True:
    arr = []
    neg = 0
    try:
        print("Ingrese un numero:")
        for x in input():
            arr.append(int(x))
    except:
        print("Ingrese un numero valido")
        print("")
    else:
        for x in range(len(arr)-1):
            if arr[x+1] == arr[x]+1 or arr[x+1] == arr[x]-1:
                pass
            else:
                neg = 1
                break
        print("")
        if neg == 1:
            print("Este numero NO es un step")
        else:
            print("Este numero SI es un step!")
        print("---------------------------------------------")


