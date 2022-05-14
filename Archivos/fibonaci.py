# Fibonacci es una secuencia en la que cada número está formado de la suma de los dos números
# anteriores de la secuencia
# Escriba una función que dado un número entero mayor o igual a 0, N, devuelve la posición N 
# de la secuencia de fibonacci.

import os

os.system("cls")

def fibonacci(numero) :        # def para definir la funcion
    if  numero == 0 :
        return 0
    elif numero == 1 :
        return 1
    return fibonacci(numero-1)+fibonacci(numero-2)
        
numero_entero = int(input("Dame un numero entero positivo: "))
print(fibonacci(numero_entero))
