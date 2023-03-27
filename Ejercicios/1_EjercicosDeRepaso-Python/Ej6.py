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