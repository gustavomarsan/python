# Crea una clase "Persona" que tenga los atributos: nombre, edad

import os
os.system("cls")

class Persona :
    def __init__(self, nom, age):
        self.nombre = nom
        self.edad   = age

    def __str__(self) -> str:
        return f"Soy {self.nombre} y tengo {self.edad} años "

    
    def saludar(self) :
        print("hola soy: ", self.nombre)

    def edades(self) :
        print("mi edad es : ", self.edad)

    def mayoriaedad(self) :
        if self.edad > 17 :
            print("Soy mayor de edad")
        else :
            print("No soy mayor de edad")

    
persona1 = Persona("Juan", 18)
persona2 = Persona("Pedro", 16)

#persona1.nombre = "Juan"
# persona1.edad =  18

print(str(persona1))
print(persona2)
#print(persona1.nombre)
#print(persona1.edad)


#persona1.saludar()
#persona1.edades()
#persona1.mayoriaedad()
#persona2.saludar()
#persona2.edades()
#persona2.mayoriaedad()