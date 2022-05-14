import os
os.system("cls")
alumnos = int(input("Cuantos alumnos tienes: "))
numperiodos = int(input("Cuantos periodos tienes: "))
matrix = [[N+1,0] for N in range(alumnos)]   #comprension de listas
if numperiodos > 1 :
    for periodo in range(numperiodos):
        matrix = [[N+1,0,0,0,0] for N in range(alumnos)]   #comprension de listas

print(matrix)
for alum in range(alumnos) :  
    for periodo in range(len(matrix[1])) : 
        print("     "+ str(matrix[alum][periodo]), end="")
    print(" ")
for periodo in range(1,len(matrix[1])) :  
    for alum in range(alumnos) : 
        matrix[alum][periodo] = input(f"Alumno {alum+1} Periodo {periodo}: ")
for alum in range(alumnos) :  
    for periodo in range(len(matrix[1])) : 
        print("     "+ str(matrix[alum][periodo]), end="")
    print(" ")