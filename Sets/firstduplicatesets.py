# Utilizando la funcionalidad genial de los sets, resuelva el problema siguiente: 
# Dada una lista de números, escribe una función "all_unique", que devuelva verdadero 
# si todos los números son únicos. Es decir, no debe haber duplicados dentro de la lista
#  para que se retorne True. Ejemplo: [1, 2, 3] -> True [1, 2, 2] -> False

import os

def firsduplicate(lista) :
    
    for num in lista :
        
        if num in setnumeros :
            return num

        else :
            setnumeros.add(num)

    return True

    
os.system("cls")

setnumeros = set()
listanumeros = [1,2,3,5,6,7,8,9,0,3]

print("First duplicate = ", firsduplicate(listanumeros))
print(listanumeros)
print(setnumeros)


