def verificarAnagrama(word1,word2):
    for x in word1:
        for y in word2:
            if x == y:
                word1 = word1.replace(x,"",1)
                word2 = word2.replace(y,"",1)
    
    if word1 == word2:
        return True
    else:
        return False

if verificarAnagrama(input("Verificacion de anagramas:\nPalabra 1:"),input("Palabra 2:")):
    print("Las palabras son anagramas!")
else:
    print("Las palabras no son anagramas :(")