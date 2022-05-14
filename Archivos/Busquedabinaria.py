# Búsqueda binaria: Dada una lista ORDENADA y un número a buscar, utiliza la técnica de búsqueda 
# binaria para escribir la función "search". Esta función deberá retornar verdadero si el elemento 
# se encuentra en la lista y falso sí no. La búsqueda binaria consiste en partir por mitad la 
# lista ordenada, para determinar si el elemento se encuentra en la parte posterior o anterior
#  en la lista, repitiendo el proceso hasta determinar si el elemento se encuentra o no.


import os
from tkinter.tix import Tree

os.system("cls")
lista=[1, 3, 4, 6, 8, 9, 11, 14, 17, 18, 20]

def busqueda(listado,numero,ini,fin) :       # def para definir la funcion
    mitad=(ini+fin)//2
    print(ini,fin,mitad)      # solo para ver como caminan los punteros ini, fin y mitad
    if fin < ini :
        return False
    if  numero == listado[mitad] :
        return True
    if numero > listado[mitad] :
        return busqueda(listado,numero, mitad+1,fin)
    return busqueda(listado,numero, ini, mitad-1)       
    

numero_buscado = int(input("Dame un numero a buscar: "))
print(busqueda(lista,numero_buscado,0,len(lista)-1))
