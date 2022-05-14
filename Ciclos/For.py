import os
os.system("cls")
lista = []
alumnos = int(input("Dame un numero de alumnos:"))
for i in range (alumnos) :
    lista.append(input(f"Dame el nombre del alumno {i+1} : "))
# numlista = [N+1 for N in range(alumnos)]   #comprension de listas    este hace lo mismo que linea 4 a 6
# numeros = [1,2,3,4,5,6,7,8,9]
# numero = 100
# for i in range(numero,numero+11, 10) :    # range(rango ini, rango fin, intervalo), (solo rango)
#       print(i,numero)
print(lista)                          # list() imprime la lista
for i in range (alumnos) :                  # range(rango ini, rango fin, intervalo), (solo rango)
     print(i+1, ".", lista[i])
tuplaalumnos=list(enumerate(lista,1))
print(tuplaalumnos)             # print con enumerate (lista,val ini), devuelve una lista de tuplas
for alumno in lista :                       # este es un for each y hace lo mismo que for i in range     
    print(alumno)
for tupla in enumerate(lista,1) :   
    numlista,alumno = tupla                 # Descompone la tupla en 2 valores     
    print(tupla)  
for numlista,alumno in enumerate(lista,1) :   # Descompone la tupla en 2 valores 
    print(numlista, alumno)   