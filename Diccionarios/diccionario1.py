# Declaracion de diccionarios
import os

os.system("cls")



diccionario = {'nombre' : 'Gustavo', 'apellidos' : 'Martinez Sanchez' , 'edad' : 50 }

print(diccionario)
print(diccionario['nombre'])
print(diccionario['edad'])

diccionario['edad'] = 40
print(diccionario['edad'])

# del diccionario['edad']

print(diccionario)
print(diccionario.values())
print(diccionario.keys())
print(diccionario.items())

for llave,valor in diccionario.items() :
    print(f"su {llave} es {valor}")
