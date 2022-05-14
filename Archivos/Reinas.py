# Poner 8 reinas en un tablero de 8 x 8 y que no se ataquen 
import os

os.system("cls")

lines = 0
count = 0
tablero = []
ejex = []
         
inkey=" "


def posible(y,x) :        # x y son coordenadas
    global tablero
        
    for i in range (lines) :
        if tablero [y][i] == 1 :
            return False
    
        if tablero [i][x] == 1 :
            return False
    cy=y
    cx=x
    while cy > 0 and  cx > 0 :      # busca de casilla hacia arriba izquierda
        cy=cy-1
        cx=cx-1
        if tablero [cy][cx] == 1 :
            return False

    cy=y
    cx=x
    while cy < lines-1 and  cx < lines-1 :      # busca de casilla hacia abajo derecha
        cy=cy+1
        cx=cx+1
        if tablero [cy][cx] == 1 :
            return False
    cy=y
    cx=x
    while cy > 0 and  cx < lines-1 :      # busca de casilla hacia arriba derecha
        cy=cy-1
        cx=cx+1
        if tablero [cy][cx] == 1 :
            return False 

    cy=y
    cx=x
    while cy < lines-1 and  cx > 0 :      # busca de casilla hacia abajo izquieda
        cy=cy+1
        cx=cx-1

        if tablero [cy][cx] == 1 :
            return False 
          
    return True

def solve() :
    global tablero
    global count
    global lines

    if count == lines :
        for n in range(lines) :
            print(tablero[n])
        return True
    
    for y in range(lines) :
        for x in range(lines) :
            
            if posible(y,x) :
                tablero[y][x] = 1
                count = count + 1
                
                if solve() :
                    return True

                tablero[y][x] = 0
                count = count - 1
    return False

lines = int(input("cuantas lineas deseas?"))
#for y in range(lines) :
#    ejex= []
#    for x in range(lines) :
#        ejex.append(0)                lo mismo que hace esta estructura lo hago en una linea abajo
#    tablero.append(ejex)

tablero = [[0 for x in range(lines)] for y in range(lines)]  # comprension de listas = con 2 ciclos

solve()

       


