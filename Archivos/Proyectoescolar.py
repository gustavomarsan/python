# Crear un programa que pregunte al usuario por la cantidad de personas que se desean registrar. 
# Después, recolectar la información para cada persona y añadir un registro por cada uno 
# en un nuevo archivo, con el nombre que quieras.
# Recomiendo utilizar el conocimiento que ya tienen sobre funciones para crear 
# una función recolectar_informacion() la cual se encargue de preguntar por la información 
# de una sola persona y devuelva una lista.

from operator import itemgetter
import os
import csv              # es de python
import capturaalumno    # para llamar mi funcion de captura de datos    
os.system("cls")

lista_alumnos = []

with open("./data/datosalumnos.csv", "r", newline = "") as csvarchivo :      #abre r para leer
    spamreader = csv.reader(csvarchivo)
    for row in spamreader :                 # recorre el archivo linea x linea 
        lista_alumnos.append(row)           # añade el registro del archivo a una lista para
                                            # vaciar el archivo a lista y trabajar en ella, al fina
                                            # grabar 
while True :
    opcion = input("Que deseas hacer? (end/add/print/update/delete): ")    
    
    if opcion == "end" :
        break

    if opcion == "add" :
        numeroalumnos = int(input("Cuantos alumnos quieres agregar: "))
        for i in range (numeroalumnos) :
            agregar =  capturaalumno.capturainfo(i)
            lista_alumnos.append(agregar)
        lista_alumnos.sort(key=itemgetter(1,2,0))

    elif opcion == "print" :
        for i, row in enumerate(lista_alumnos) :           # obtengo en i el numero de ciclo
            print(i+1, row[0], row[1], row[2], "calificacion :", row[3])
    
    elif opcion == "update" :
        num_lista_cambio = int(input("Numero de lista de alumno a modificar calificacion: "))
        nueva_cali = float(input("Dame la nueva calificacion: "))
        lista_alumnos[num_lista_cambio-1][3] = nueva_cali
    
    elif opcion == "delete" :
        num_lista_baja = int(input("Numero de lista de alumno a borrar: "))
        lista_alumnos.pop(num_lista_baja-1)

    else :
        print("******Opcion no valida******")
with open("./data/datosalumnos.csv", "w", newline = "") as csvarchivo :      #abre w para sobreescribir
    spamwriter = csv.writer(csvarchivo)
    spamwriter.writerows(lista_alumnos)           # guardamos todas las filas al mismo tiempo