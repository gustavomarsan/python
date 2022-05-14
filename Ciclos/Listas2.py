import os
os.system("cls")
alumnos = int(input("Cuantos alumnos tienes: "))
calificacion = [10] * alumnos
print(calificacion)
numlista = [N+1 for N in range(alumnos)]   #comprension de listas
print(numlista)
# numlista.reverse()
# print(numlista)
# numlista.extend(lista)                      #extend agrega al final elementos de una lista 1 x 1
# print(numlista)
# numlista.append(lista)                      #append agrega al final elementos de una lista como 1 elem
for x in range(alumnos) :
       calificacion[x] = input(f" Calificacion alumno {x+1} : ")
print("Num lista    Calificacion")
for x in range(alumnos) :
    print(numlista[x], "            ", calificacion[x])
