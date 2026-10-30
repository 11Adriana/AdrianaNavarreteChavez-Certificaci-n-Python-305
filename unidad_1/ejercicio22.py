try:
    # DECLARAMOS LAS LISTAS
    alumnos = ["Vanessa", "Emmanuel", "Julio", "Paola",
               "Rosalia", "Francisco", "Adriana",
               "Maximiliano", "Juan Carlos"]

    calificaciones = [9, 8, 10, 9, 7, 8, 10, 9, 8]

    
    for i in range(len(alumnos)):
        print("Alumno:", alumnos[i])
        print("Calificacion:", calificaciones[i])

except IndexError:
    print("Indice incorrecto")

else:
    print("Lista mostrada correctamente")

finally:
    print("Programa finalizado")