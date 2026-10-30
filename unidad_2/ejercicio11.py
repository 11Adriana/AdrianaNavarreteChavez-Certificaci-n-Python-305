alumnos=[]
calificacion=[]
cantidad=int(input("¿Cuantos alumnos quieres agregar?"))
for contador in range (cantidad):
    nombre=input("Registra el nombre de los alumno:")
    calificaciones=int(input("Registra el promedio de los alumnos:"))
    alumnos.append(nombre)
    calificaciones.append(calificacion)
print("\nLista de alumnos:")
print(alumnos)

print("\nlista de calificaciones:")
print(calificacion)
calificacion_alta=contador[0]
calificacion_baja=contador[0]
for contador in calificacion:
    if contador>calificacion_alta:
        calificaciion_alta=contador

        
    if contador<calificacion_baja:
        calificacion_baja=contador

        
            

print("El promedio mas alto es ",calificacion_alta)
print("El promedio mas bajo es ",calificacion_baja)




