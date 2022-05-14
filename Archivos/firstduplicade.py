# Dada una lista de números, escribe una función "first_duplicate", que devuelva el primer número 
# duplicado de la lista. El primer duplicado se define como el número que tiene su segunda 
# aparición primero.
 
 
import os

os.system("cls")

def primerduplicado(lista) :        # def para definir la funcion
    for n in range (1,len(lista)) :
        for y in range (0,n) :
            if lista[n] == lista[y] :
                return lista[n]
    return None


cadena_num = input("Dame el string de numeros a revisar: ")
print(primerduplicado(cadena_num))

