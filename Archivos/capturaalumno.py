# Este programa es una funcion que captura datos y regresa una lista

def capturainfo(numal) :        # def para definir la funcion que captura info, nom ape par, ape mat, edad
    lista=[]
    nombre = input(f"Dame el Nombre del Alumno {numal+1}: " )
    lista.append(nombre)
    apaterno = input("Dame el Apellido Paterno: ")
    lista.append(apaterno)
    amaterno = input("Dame el Apellido Materno: ")
    lista.append(amaterno)
    calificacion = float(input("Dame la calificacion: "))
    lista.append(calificacion)
    return lista          # devuelve el resultado