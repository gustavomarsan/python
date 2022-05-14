# Utilizando el módulo csv de python (https://docs.python.org/3/library/csv.html ), 
# crear archivos separados por comas con writer.
# En esta ocasión, utilizar la sintaxis con with

import os
import csv

os.system("cls")

with open("./data/personales.csv", "w", newline = "") as csvarchivo :
    spamwriter = csv.writer(csvarchivo, delimiter = ",", 
                            quotechar= "\"" , quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["NOMBRE", "APELLIDO PATERNO", "APEDILLO MATERNO", "EDAD"] )
    spamwriter.writerow(["Gustavo Dario", "Martinez", "Ramos", "22"] )

