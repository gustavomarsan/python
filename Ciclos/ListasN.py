import os
os.system("cls")
alumnos = int(input("Cuantos alumnos tienes: "))
lista = [10] * alumnos
print(lista)
numlista = [N+1 for N in range(alumnos)]   #comprension de listas
print(numlista)
# numlista.append(64)
print(numlista)
# numlista.extend(lista)
print(numlista)
print(lista)
lista.insert(3, 50)                             # insert(poscion, dato)
print(lista)
print(lista.pop(3))                             # pop borra registro especifico
print(lista)
numlistaalreves=numlista.copy()                 # copia lista 
numlistaalreves.reverse()
print(numlista)
print(numlistaalreves)
numlista.sort()
print(numlista)
print(numlista)
if 8 not in numlista and 18 not in numlista :   #in y not in se refiere a si pertenece a la lista
    print("NO ESTAN NINGUNO DE LOS 2 ")
elif 8 not in numlista or 18 not in numlista : 
    print("SI ESTA AL MENOS 1")
else :
    print("SI ESTAN LOS DOS")
print(len(numlista))                # len devuelve la longitd de la lista
print(numlista)
print(list(reversed(numlista)))     #list mete en lista el reversed de numlista 
print(max(numlista))
print(min(numlista))
print(sum(numlista,0))              # sum(lista, parametro) suma los valores de la lista y añade el parametro 
print("EL PROMEDIO ES: ", sum(numlista)/len(numlista))