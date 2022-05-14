# Ejemplo de funcion con retorno
import os
os.system("cls")

def suma(a,b):          # def para definir la funcion que suma los 2 parametros
    return a+b          # devuelve el resultado

if __name__ == "__main__":   # solo correra si estory corriendo este programa, no si lo referencio para funciones a otros programas
    suma1= int(input("Dame el primer numero a sumar : "))
    suma2= int(input("Dame el segundo numero a sumar: "))
    print(suma(suma1, suma2))   # llama la funcion suma con 2 parametros
