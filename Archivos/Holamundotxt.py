#Abre el archivo de texto "./data/hola_mundo.txt" en modo escritura. 
# Escribe dentro del archivo "Hola mundo"

import os
os.system("cls")

f=open("./data/hola_mundo.txt","wt")    # abre un archivo en modo escritura(w) y forma texto(t)
f.write("Hola mundo")
f.close()                               # cierra el archivo