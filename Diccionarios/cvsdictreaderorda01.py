
import os
import csv

def obten_modelo (orden) :
    return orden['O1_NUMMOD']


os.system("cls")

ordenes = []

with open('./data/orda01.csv', 'r' , newline = "") as csvfile :
    spamreader = csv.DictReader(csvfile)

    for row in spamreader :                 # recorre el archivo linea x linea 
        row["O1_NUMORD"] = int(row["O1_NUMORD"])
        row["O1_NUMMOD"] = int(row["O1_NUMMOD"])
        ordenes.append(row)
    
ordenes.sort(key=obten_modelo)

while True :
    os.system("cls")
    opcion = input("Que deseas hacer? (orden/ordenes/end): ")    
    
    if opcion == "end" or opcion == "END" :
        break
    
    if opcion == "ordenes" or opcion == "ORDENES":
        nummod = int(input("Dame el Numero de modelo :"))
        
        for row in ordenes :
                        
            if nummod == row["O1_NUMMOD"] :
                print(str(row['O1_NUMORD']).rjust(3,"0"), row['O1_NUMMOD'], row['O1_DESCRP'].ljust(15)[0:14],
                          row['O1_NOMTEL'].rjust(15)[0:14], "Fecha :", row['O1_FECORD'], 
                        "Cancela: ", row['O1_FECINI'],)
        
        input("press any key to continue")

    if opcion == "orden" or opcion == "ORDEN" :
        numord = int(input("Dame el Numero de orden  :"))
        nummod = int(input("Dame el Numero de modelo :"))

        for row in ordenes :
            if nummod == row['O1_NUMMOD'] and row['O1_NUMORD'] == numord :
                print(row['O1_DESCRP'] , row['O1_NOMTEL'] )
                print("Autorizada: ", row['O1_CLAAUT'] )
                print("Graduada:   ", row['O1_CLAGRA'] )
                print("Cortada:    ", row['O1_CLACOR'], row['O1_CANCOR'] )
                print("Armada:     ", row['O1_CLAARM'], row['O1_CANARM'] )
                print("Terminada:  ", row['O1_CLATER'], row['O1_CANTER'] )
                if row['O1_CLACAN'] == "S" :
                    print("* * * * * * * * * * O R D E N      C A N C E L A D A * * * * * * * * * *")
                if row['O1_CLACOM'] == "S" :
                    print("* * * * * * * * * * O R D E N      C O M P R A D A * * * * * * * * *")
            exit    
        input("press any key to continue")
        