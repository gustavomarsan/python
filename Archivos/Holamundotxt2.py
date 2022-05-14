#Pide al usuario el nombre de un archivo de texto y abrelo en modo escritura.
#Después, pide al usuario lo que quiere que se escriba en este archivo.

import os
os.system("cls")

archivo= (input("Dame el nombre del archivo a abrir : "))
texto= (input("Dame el texto a escribir en el archivo : "))
f=open(f"./data/{archivo}.txt","wt")    # abre un archivo en modo escritura(w) y forma texto(t)
f.write(texto)                          # agrega texto al archivo
f.close()                               # cierra el archivo