# Este programa es una funcion que captira dapts y regresa una lista

def capturainfo(numal) :        # def para definir la funcion que captura info, nom ape par, ape mat, edad
    lista=[]
    nombre = input(f"Dame el Nombre del alumno {numal+1}: " )
    lista.append(nombre)
    apaterno = input("Dame el Apellido Paterno: ")
    lista.append(apaterno)
    amaterno = input("Dame el Apellido Materno: ")
    lista.append(amaterno)
    edad = input("Dame la edad: ")
    lista.append(edad)
    return lista          # devuelve el resultado