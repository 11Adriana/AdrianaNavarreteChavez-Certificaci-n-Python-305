#ciclo externo para el numero de l base de la tabla
for i in range(1,4):
    print(f"---Tabla del {i} ---")
    #Ciclo interno para multiplicardel1 al 10
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")
        #aqui sale del ciclo interno 
    print(f"AQUI TERMINA LA TABLA DEL {i}")

#1(1 ) x 1(j)=1
