colores=["azul", "rojo", "amarillo", "morado", "naranja"]
color=input("Ingresa el color: ")
encontrado=False
for contador in colores:
    print(contador)
    # Si el color ingresado coincide, detener el bucle
    if contador==color:
        print("Color encontrado, saliendo del bucle")
        encontrado=True
        break
if not encontrado:
    print("El color", color, "no se ha encontrado")
