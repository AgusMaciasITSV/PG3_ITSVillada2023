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