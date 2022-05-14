# Declaracion de diccionarios
import os
import csv

os.system("cls")



with open('./data/alumnos.csv', 'r' , newline = "") as csvfile :
    reader = csv.DictReader(csvfile)

    for row in reader :
        for llave,valor in row.items() :
            print(llave,":", valor)
        #print(row['Apellido paterno'])
        #print(row['Apellido materno'])
        #print(row['Nombre'])
        #print(row['Calificacion'])