while True:
    rwrd = ""
    print("Escriba una palabra para averiguar si es un palindromo:")
    wrd = input()
    rwrd = wrd[::-1]
    print(rwrd)
    if wrd == rwrd:
        print("Su palabra SI es un palindromo.")
    else:
        print("Su palabra NO es un palindromo.")
    print("")