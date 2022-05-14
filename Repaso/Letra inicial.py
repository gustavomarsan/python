# Escribe un programa que lea un numero N, y lea N nombres de alumnos.
# Después, el programa recibirá una letra del abecedario y deberá imprimir 
# un nombre (solo uno) que comience con esta letra. Si no lo encuentra imrimir "fulanito"
import os
os.system("cls")
fulanito = False        # bandera para saber si encontro un nombre con esa inicial
listaalumnos = []
numeroalumnos = int(input("Cuantos alumnos son: "))
for i in range (numeroalumnos) :
    listaalumnos.append(input("Dame el nombre del alumno :"))
inicial = str(input("Dame letra inicial: "))
for alumno in range(numeroalumnos) :
    if listaalumnos[alumno].startswith(inicial) : # la funcion startswith compara el inicio de una cadena y devuelve valor true or false
        fulanito = True     # bandera para saber si encontro un nombre con esa inicial
        print(listaalumnos[alumno])
        break               # solo queremos imprimir un nombre por lo que tronamos el ciclo al encontrarlo
if not fulanito:
    print("Fulanito ")      # si no se encuentra la inicial en la cadena 
