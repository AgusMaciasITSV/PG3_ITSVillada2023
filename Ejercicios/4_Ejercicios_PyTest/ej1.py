import re

def validate_password(password):
    U = False
    L = False
    N = False
    if len(password) < 8:
        return False
    
    elif checkSpecialChars(password) == False:
        return False
    
    else:
        for x in password:
            if x.isupper() is True:
                U = True
            elif x.islower():
                L = True
            elif x in ["0","1","2","3","4","5","6","7","8","9"]:
                N = True
            
    if U and L and N:
        return True
    else:
        return False

def checkSpecialChars(string):

    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') #Se definen los caracteres especiales
  
    if(regex.search(string) == None):
        return True     
    else:
        return False

if validate_password(input("Ingrese su contraseña, al menos debe tener:\n*8 caracteres\n*Una mayúscula\n*Una minúscula\n*Un numero\n*No puede poseer caracteres especiales\n")):
    print("Contraseña valida")
else:
    print("Contraseña no válida")
