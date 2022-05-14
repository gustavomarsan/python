#Escribe un programa que reciba una conjunto de números e imprima el más grande. 
# El programa debera leer números hasta que el usuario escriba "Fin". Después, 
# el programa debera contestar con la respuesta
import os
os.system("cls")
continuar = True
numeromayor= float("-inf")
while continuar :
    numero = input("Dame un numero :")
    if numero in ["Fin" , "fin" , "FIN"] :
        continuar = False
    else :
        numeromayor = max(numeromayor,int(numero))      #funcion max devuelve valor maximo 
print(numeromayor)