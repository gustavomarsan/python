nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))
vivecon = input(" vives con tus papas (S/N)? ")
permiso = input(nombre + ", ¿tienes permiso de tus papas para beber alcohol (S/N)? ") 
mayor_de_edad = edad > 17
tiene_permiso = permiso == "S"
vive_con_papas = vivecon == "S"
if mayor_de_edad and ( tiene_permiso or not vive_con_papas ) :
    print(nombre + " eres afortunado!!!! tienes mi autorizacion para tomar alcohol   :)")
else :
    print(nombre + " lo siento mucho pero no tienes mi autorizacion para tomar alcohol :(")
print("Gracias por participar")
