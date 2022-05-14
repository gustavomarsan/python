# Escriba una función que reciba un número entero positivo N y imprima desde N  hasta 0 
# de forma descendente. Esta función no debe utilizar while ni for. Para lograrlo, deberá llamar
# a la misma función recursivamente.

import os

os.system("cls")

def hasta_cero(numero) :        # def para definir la funcion
    if numero <= 0 :
        return
    print(numero)
    hasta_cero(numero-1)
        
numero_entero = int(input("Dame un numero entero positivo: "))
hasta_cero(numero_entero)