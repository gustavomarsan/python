#Escribe un programa que reciba una conjunto de números e imprima el más grande. 
# El programa debera leer números hasta que el usuario escriba "Fin". Después, 
# el programa debera contestar con la respuesta
import os
os.system("cls")
lista = []
continuar = True
while continuar  :
    numero = input("Dame un numero :")
    if numero in ["fin", "Fin", "FIN"] :
        continuar = False
    else :
        lista.append(int(numero))
print(max(lista))      # funcion max devuelve numero mayor de un iterable o grupo de valores