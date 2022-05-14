# Abre el archivo "./data/hola_mundo.txt" en modo lectura e imprime su contenido en pantalla.

import os
os.system("cls")

texto = "."

f=open("./data/hola_mundo.txt","r")    # abre un archivo en modo lectura(r)
texto = f.read()                         # read lee el archivo
print(texto)
f.close()                                    # cierra el archivo