# Escribe una función que dado un string, retorna el primer caracter que no se repita.
# Ej.    "abacad" -> b
# Ej.2   "adacad" -> c
 
import os
os.system("cls")

def not_dupli(elementos) :                   # recibo cadena
   
    dic_carac = {}                           # declaro dict con cada caracter de la cadena
    for x in elementos :                     # recorro la cedana y asigno repeticiones en el dict
        if x in dic_carac :
            dic_carac [x] += 1
        else  : 
            dic_carac[x] = 1
    
   
    print(dic_carac)                         # verificacion 
    print(elementos)                         # verificacion 
    for x in elementos :                     # busco el primero no repetido, solo un elemento, osea no dupli
        if dic_carac[x] == 1 :
            return x                         # regreso el primero no dupli

cadena = "martinezramos"
print("El primer no duplicado es :", not_dupli(cadena))


