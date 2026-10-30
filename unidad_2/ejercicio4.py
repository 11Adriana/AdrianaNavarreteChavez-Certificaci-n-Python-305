promedio=[9,10,6,5,7]
#crea lista
#1.ENCONTRAR EL PROMEIO MAS BAJO USANDO CICLO FOR 
#SUPONEMOS QUE INICIALEMTE QUE EL PROMEDIO MAS BAJO ES EL PRIMER ELEMEMTO 
promedio_alto=promedio[0]
promedio_bajo=promedio[0]

#promedio bajo paramentro
#contador obtien los valores de la slita prmedio
for contador in promedio:
    if contador>promedio_alto:
        promedio_alto=contador

        
    if contador<promedio_bajo:
        promedio_bajo=contador

        
            

print("El promedio mas alto es ",promedio_alto)
print("El promedio mas bajo es ",promedio_bajo)



