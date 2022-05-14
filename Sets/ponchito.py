# En el colegio Anáhuac, Ponchito quiere saber cuántos alumnos reprobados hay en la prepa.
# Sin embargo, tiene el problema de que solamente tiene las listas de los reprobados por materia.
# Esto es problemático porque varios alumnos (como Petacas y Sofo) aparecen en más de una lista
# de reprobados. Ayuda a ponchito escribiendo una función que reciba la lista de todos
# los reprobados por materia y retorne la cantidad de alumnos DIFERENTES reprobados.
# Ejemplo: ["JUAN", "JUAN", "PEDRO", "PEDRO", "LUISA"] -> 3
# Tip: se puede utilizar set comprehensions para resolver este problema en una sola línea.

import os
os.system("cls")

def num_repro(lista) :
    repro_col = {x for x in lista } 
    return len(repro_col)

repro_mat = []
print("Captura los alumnos reporbados de todas las materias, exit para salir")
alumno = " "
while alumno != "exit" :
    alumno = input("Dame el nombre del alumno: ") 
    if alumno != "exit" :
        repro_mat.append(alumno) 

#print(repro_mat)
print("Total de alumnos reprobados: ", num_repro(repro_mat))