# Declaracion de diccionarios
import os
import csv

os.system("cls")


def capturainfo(numal) :        # def para definir la funcion que captura info, 
    datos = {}
    datos['Nombre'] = input(f"Dame el Nombre del Alumno {numal+1}: " )
    datos['Apellido paterno'] = input("Dame el Apellido Paterno: ")
    datos['Apellido materno'] = input("Dame el Apellido Materno: ") 
    datos['Calificacion'] = float(input("Dame la calificacion: "))
    return datos          # devuelve el resultado


with open('./data/alumnos.csv', 'w' , newline = "") as csvfile :
    encabezados = ['Apellido paterno' , 'Apellido materno', 'Nombre', 'Calificacion']
    writer = csv.DictWriter(csvfile, fieldnames= encabezados)

    writer.writeheader()
    numeroalumnos = int(input("Cuantos alumnos quieres agregar: "))

    for n in range(numeroalumnos) :
        writer.writerow(capturainfo(n))
