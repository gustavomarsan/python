#Escribe un programa que reciba una conjunto de números e imprima el tercero más grande. 
# El programa debera leer números hasta que el usuario escriba "Fin". 
# Después, el programa debera contestar con la respuesta.
import os
os.system("cls")
lista = []
continuar = True
while continuar  :
    numero = input("Dame un numero :")
    if numero in ["fin", "Fin", "FIN", "x", "X", "", " "] :
        continuar = False
    else :
        lista.append(int(numero))
lista.sort()                    #ordena la lista con funcion sort
print(lista[(len(lista)-3)])    # obtiene el antepenultimo valor de la lista