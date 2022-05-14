# Pide al usuario el nombre de un archivo de texto y abrelo en modo escritura.
# Después, pide al usuario lo que quiere que se escriba en este archivo. En este ejercicio, 
# se recopilarán y escribirán en el archivo las líneas que el usuario ingrese,
# hasta que este escriba "Fin".

import os
os.system("cls")
texto = "."
archivo= (input("Dame el nombre del archivo a abrir : "))
f=open(f"./data/{archivo}.txt","wt")    # abre un archivo en modo escritura(w) y forma texto(t)

while True :
    texto= (input("Dame el texto a escribir en el archivo : "))
    if texto in ["fin", "Fin", "FIN", ""] :
        break
    f.write(texto+"\n")                      # agrega texto al archivo  , \n es salto de linea                
f.close()                                    # cierra el archivo