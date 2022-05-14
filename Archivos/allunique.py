# Dada una lista de números, escribe una función "all_unique", que devuelva verdadero 
# si todos los números son únicos. Es decir, no debe haber duplicados dentro de la lista
# para que se retorne True 
 
import os

os.system("cls")

def unicos(lista) :        # def para definir la funcion 
    for n in range (len(lista)-1) :
        for y in range (n+1,len(lista)) :
            if lista[n] == lista[y] :
                return False
    return True

cadena_num = input("Dame el string de numeros a revisar: ")
print(unicos(cadena_num))

