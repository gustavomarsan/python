# Cuenta regresiva hasta cero a partir de un numero

import os

os.system("cls")

def cuenta_regresiva(numero) :        # def para definir la funcion
    numero = numero -1 
    if numero > 0 :
        print(numero)
        cuenta_regresiva(numero)
    else :
        print("booom")

numero_entero = int(input("Dame un numero entero positivo: "))
cuenta_regresiva(numero_entero)
