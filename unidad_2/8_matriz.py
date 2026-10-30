#listas_colores=["azul","rojo"]
#creando una matriz
matriz=[
    [5,8,6],#Fila0 #3 columnas #0
    #0,1,2
    [3,9,4]#fila1 #3 columnas #1
    #1,2,3
]
#obteniendo el numero tota de filas y columnas 
#filas=len(matriz) # solo tomando esa me dice cuatas tengo cuanta los corchetes 
#columnas=len(matriz[0])
#ciclo externo para los indices de las filas (i)
for i in range(0,2):
    #ciclo interno par los indices de las columnas(j)
    for j in range(0,3):
        print(f"posicion[{i}][{j}]={matriz[i][j]}")


