# Crear un programa que pregunte al usuario por la cantidad de personas que se desean registrar. 
# Después, recolectar la información para cada persona y añadir un registro por cada uno 
# en un nuevo archivo, con el nombre que quieras.
# Recomiendo utilizar el conocimiento que ya tienen sobre funciones para crear 
# una función recolectar_informacion() la cual se encargue de preguntar por la información 
# de una sola persona y devuelva una lista.
# pero con la funcion writerows (guarda filas en una sola operacion)


import os
import csv              # es de python
import capturadatos     # para llamar mi funcion de captura de datos    
os.system("cls")
agregar=[]
numeroalumnos = int(input("Cuantos alumnos quieres agregar: "))

with open("./data/personalesrow.csv", "a+", newline = "") as csvarchivo :      #abre a+ para agregar
    spamwriter = csv.writer(csvarchivo)
    for i in range (numeroalumnos) :
        agregar.append(capturadatos.capturainfo(i))
    spamwriter.writerows(agregar)           # guardamos todas las filas al mismo tiempo

