def search_matrix(matrix, target):
    for x in matrix:
        if x == target:
            return True
    return False

matrix = [3,2,"Hola",True,3.14]
target = True

if search_matrix(matrix,target):
    print("El ojetivo si se encuentra en la matriz.")
else:
    print("El objetivo no se encuentra en la matriz.")