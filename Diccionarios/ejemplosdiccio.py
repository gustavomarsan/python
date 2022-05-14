# Declaracion de diccionarios
import os

os.system("cls")



diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }

print(diccionario)
print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'])
if "pais" in diccionario :
    print(diccionario['pais'])
else :
    print("No existe el campo PAIS")
    diccionario['pais']= "Mexico"
print(diccionario)