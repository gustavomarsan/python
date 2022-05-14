# Pide al usuario un nombre de archivo, abrelo en modo lectura e imprime su contenido en pantalla.

import os
os.system("cls")

archivo= (input("Dame el nombre del archivo a abrir : "))
f=open(f"./data/{archivo}.txt","rt")   # abre un archivo en modo lectura(r)
texto = f.read()                       # read lee el archivo
print(texto)
f.close()                              # cierra el archivo