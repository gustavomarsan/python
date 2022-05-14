# Resuelve un Sudoku con recurrencia

import os
# import numpy as np

os.system("cls")

sudoku = [[0,0,4,9,3,0,6,0,0],
          [0,6,0,8,0,2,0,0,0],
          [0,1,0,4,0,0,0,5,0],
          [2,5,6,7,9,3,8,0,0],
          [1,4,8,2,5,6,3,0,0],
          [7,3,9,1,8,4,0,6,0],
          [3,0,1,5,0,0,0,9,0],
          [4,0,0,0,0,0,0,0,0],
          [6,0,0,0,0,0,0,0,0]]
          
          

def posible(y,x,n) :        # x y son coordenadas, n es numero a buscar si es posible
    global sudoku
    for i in range (9) :
        if sudoku [y][i] == n :
            return False
    for i in range (9) :
        if sudoku [i][x] == n :
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3

    for i in range (y0, y0+3) :
        for j in range (x0, x0+3) :
            if sudoku [i][j] == n :
                return False
    return True

def solve() :
    global sudoku
    #print(sudoku)
    for y in range(9) :
        for x in range(9) :
            if sudoku[y][x] == 0 :
                for n in range (1,10) :
                    if posible(y,x,n) :
                        sudoku[y][x] = n
                        solve()

                        sudoku[y][x] = 0
                return
    for n in range(9) :
        print(sudoku[n])


for n in range(9) :
    print(sudoku[n])
print("--------------------")
solve()



                


