# programa para funciones creadas por el programador. Primero se definen y despues se llaman las
# veces que se quiera. Puede llamarse con parametros o sin parametros.
# estas funciones son SIN RETORNO
import os
from pickle import TRUE
os.system("cls")

def saludar() :             # def es para definir una funcion def(par1, par2, par3)
    print("Hola")

def saludarname(nombre) :
    print("Hola ",nombre)

def mayoredad(name,age) :
    if age > 17 :
        print("Hola ", name, " ya puedes tomar alcohol :)")
    else :
        print("Hola ", name, " aun no puedes tomar alcohol :(")

nom = input("Dame el nombre: ")
edad = int(input("Dame la edad: "))

saludar()                    # llama la funcion sin parametros
saludarname(nom)             # llama la funcion con un parametro
mayoredad(nom,edad)          # llama la funcion con dos parametros