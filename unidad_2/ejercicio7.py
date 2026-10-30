#EL MAPA DEL TESORO
mapa=[
     #o, #1, #2, #3,
    [".",".",".","."],#0
    [".",".","B","."],#1
    [".",".",".","X"],#2
    [".",".",".","."],#3
    

]
filas=len(mapa)
columnas=len(mapa[0])
#recorriendo la matriz con ciclos anidados
#ciclo ecterno para manejar filas (i)
for i in range(filas):
    #ciclo externo para ,njar columnas 
    for j in range(columnas):
        #verificacmos si encontramos el tesoro
        if mapa[i][j]=="X":#[0][0]
        
            print(f"TESORO ENCONTRADO EN LA POSICION [{i}][{j}] ")
        if mapa[i][j]=="B":#[0][0]
        
            print(f"TESORO ENCONTRADO EN LA POSICION [{i}][{j}] ")


