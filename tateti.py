import random
#tablero
def mostrar_tablero(tablero):
    linea_horizontal = "+-------+-------+-------+"
    linea_vacia = "|       |       |       |"

    for i in range(3):
            print(linea_horizontal)
            print(linea_vacia)
            print(f"|   {tablero[i*3]}   |   {tablero[i*3+1]}   |   {tablero[i*3+2]}   |")
            print(linea_vacia)
            
    print(linea_horizontal)

def revisar_ganador(tablero, letra):
    lineas_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]             
    ]
    for linea in lineas_ganadoras:
        if tablero[linea[0]] == tablero[linea[1]] == tablero[linea[2]] == letra:
            return True
    return False

mi_tablero = [1,2,3,4,5,6,7,8,9]
while True:
    casilleros_libres = []
    for casilla in mi_tablero:
         if  casilla !="X" and casilla!="O":
              casilleros_libres.append(casilla)       

    #usuario
    mostrar_tablero(mi_tablero)
    movimiento = int(input("Ingrese un casillero: "))
    while movimiento not in casilleros_libres:
        mostrar_tablero(mi_tablero)
        print("Esa casilla esta ocupada elija otra")
        movimiento = int(input("Ingrese un casillero: "))

    jugada_us= movimiento -1
    mi_tablero[jugada_us] = "X"
    print(f"Eleguiste jugar en el casillero {movimiento}")

       

    if revisar_ganador(mi_tablero, "X"):
        mostrar_tablero(mi_tablero)
        print("¡FELICIDADES, GANASTE!")
        break 

    #PC 
    if len(casilleros_libres) == 0:
        mostrar_tablero(mi_tablero)
        print("¡HAY EMPATE! Se llenó el tablero.")
        break # Corta el ciclo

    jugada_pc = random.choice(casilleros_libres)
    jugada_m= jugada_pc -1
    mi_tablero[jugada_m] = "O"

    print(F"La computadora elijio jugar en el casillero {jugada_pc}")

    if revisar_ganador(mi_tablero, "O"):
            mostrar_tablero(mi_tablero)
            print("LA COMPUTADORA GANA.")
            break



