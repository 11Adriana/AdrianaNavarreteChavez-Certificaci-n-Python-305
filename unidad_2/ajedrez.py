# 1. Definimos las piezas iniciales del ajedrez en una matriz 8x8
# 'T': Torre, 'C': Caballo, 'A': Alfil, 'D': Dama, 'R': Rey, 'P': Peón
# Las minúsculas son piezas negras, las mayúsculas son blancas, '.' son casillas vacías.

tablero = [
    ['t', 'c', 'a', 'd', 'r', 'a', 'c', 't'],  # Fila 0 (Piezas negras principales)
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  # Fila 1 (Peones negros)
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Fila 2 (Casillas vacías)
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Fila 3 (Casillas vacías)
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Fila 4 (Casillas vacías)
    ['.', '.', '.', '.', '.', '.', '.', '.'],  # Fila 5 (Casillas vacías)
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # Fila 6 (Peones blancos)
    ['T', 'C', 'A', 'D', 'R', 'A', 'C', 'T']   # Fila 7 (Piezas blancas principales)
]

print("--- REPRESENTACIÓN DEL TABLERO DE AJEDREZ ---")

# 2. Ciclos anidados para recorrer la matriz
# Ciclo externo: Recorre cada fila del tablero
for i in range(len(tablero)):
    
    # Ciclo interno: Recorre cada elemento (columna) dentro de esa fila
    for j in range(len(tablero[i])):
        # Imprimimos cada pieza o espacio separado por un espacio, sin saltar de línea
        print(tablero[i][j], end=" ")
        
    # Salto de línea al terminar de imprimir una fila completa
    print()