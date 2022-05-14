# Ejemplo de funcion con retorno
# recibe 2 numeros y los multiplica pero sin usar el operando *
import os
import Funcionretorno   #importa otro programa para poder usar funciones de este
os.system("cls")

def producto(a,b):          # def para definir la funcion que suma los 2 parametros y devuelve resultado
    result = 0
    for i in range(b) :
        result = Funcionretorno.suma(result,a)    #utilizo una funcion de otro programa ya importado
    return result           # devuelve el resultado    

if __name__ == "__main__" : # solo correra si estory corriendo este programa, no si lo referencio para funciones a otros programas
    num1= int(input("Dame el primer numero a multiplicar : "))
    num2= int(input("Dame el segundo numero a multiplicar: "))
    print(producto(num1, num2))      # llama la funcion suma con 2 parametros y devuelve valor