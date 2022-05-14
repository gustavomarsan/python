# Hacer un programa que lea el archivo que se creo que en el ejercicio de la sección anterior.
#  Por cada registro, deberá imprimir:
# "{Nombre completo, empezando por apellidos}, {edad} años de edad."

import os
import csv              # es de python
os.system("cls")
with open("./data/personalesrow.csv", "r", newline = "") as csvarchivo :      #abre r para leer
    spamreader = csv.reader(csvarchivo)
    for row in spamreader :
        print(row[1], row[2], row[0], row[3], "años de edad")
