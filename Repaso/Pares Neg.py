#Escribe un programa que imprima los numeros del 2 al 20, imprimiendo solamente los números pares.
import os
from pickle import APPEND
os.system("cls")
lista = []
for i in range(-20, 3, 2) :
    lista.append(i)
lista.reverse()
for num in lista :
    print(num)