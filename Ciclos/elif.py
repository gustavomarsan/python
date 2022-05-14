nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))
if edad > 20 :
    print(nombre, "eres mayor de edad en Mexico y en USA")
elif edad > 17:
    print(nombre, "eres mayor de edad solo Mexico y no en USA")
else :
    print(nombre, "no eres mayor de edad ni en Mexico ni en USA")
print("Gracias por participar")
