alumnos=[]
calificaciones=[]

cantidad=int(input("¿Cuántos alumnos quieres agregar?"))

for contador in range(cantidad):
    nombre=input("Registra el nombre de los alumnos:")
    calificacion=int(input("Registra el promedio de los alumnos:"))
    alumnos.append(nombre)
    calificaciones.append(calificacion)

print("\nLista de alumnos:")
print(alumnos)

print("\nLista de calificaciones:")
print(calificaciones)

calificacion_alta=calificaciones[0]
calificacion_baja=calificaciones[0]

for contador in calificaciones:
    if contador > calificacion_alta:
        calificacion_alta=contador

    if contador < calificacion_baja:
        calificacion_baja=contador

print("El promedio más alto es",calificacion_alta)
print("El promedio más bajo es",calificacion_baja)