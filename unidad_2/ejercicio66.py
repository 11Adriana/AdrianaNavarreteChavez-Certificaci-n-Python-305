#[A,B,C,D]
#[A,B,C,D]
#[A,B,C,D]
#[A,B,C,D]
# HACER UNA MATRIZ EN LA CUAL SE COLOCA EL ABECEDARIO CON FIAS Y COLUMNAS 
abecedario=[
    ["A","B","C","D"],
    ["E","F","G","H"],
    ["I","J","K","L"],
    ["M","N","O","P"],
    ["Q","R","S","T"],
    ["U","V","W","X"],
    ["Y","Z"," "," "],
]

for i in range(0,7):
    #ciclo interno par los indices de las columnas(j)
    for j in range(0,4):
        print(f"posicion[{i}][{j}]={abecedario[i][j]}")

