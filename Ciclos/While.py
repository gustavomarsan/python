import os
os.system("cls")
numero = 100
password = "LN3COL19"
enterkey = ""
veces = 0
while enterkey != password and veces < 5 :
    enterkey = input("PASWWORD: ")
    veces += 1
if enterkey == password:
    print("ACCESO CORRECTO")
    for i in range(numero,numero+101, 10) :    # range(rango ini, rango fin, intervalo), (solo rango)
        print(i,numero)
else :
    print("ACCESO DENEGADO")