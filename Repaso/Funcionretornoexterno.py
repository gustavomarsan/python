# Ejemplo de funcion con retorno
import os
os.system("cls")
import Funcionmate   #importa otro programa para poder usar funciones de este


suma1= int(input("Dame el primer numero : "))
suma2= int(input("Dame el segundo numero : "))
print("La suma de tus numeros es :", Funcionmate.suma(suma1, suma2))   # llama la funcion suma con 2 parametros y esta en el programa funcionmate
print("El producto de tus numeros es :", Funcionmate.multiplica(suma1, suma2))   # llama la funcion suma con 2 parametros y esta en el programa funcionmate

