# Escribe una función que reciba un string y devuelve si es un palíndromo.
# Un palíndromo es una palabra que se escribe igual en ambos sentidos

import os

os.system("cls")

def palindromo(lista) :        # def para definir la funcion 
    #palin = True
    for n in range (len(lista)//2) :
        if lista[n] != lista[-1-n] :
            return False
    return True


cadena = input("Dame el string a revisar: ")
print(palindromo(cadena))



