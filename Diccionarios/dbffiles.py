# este programa importa archivo dbf a python
import os
from dbfread import DBF

os.system("cls")


for orden in DBF('./data/ORDA01.dbf'):
    print(orden['O1_NUMORD'])
    print(type(orden['O1_NUMORD']))
    