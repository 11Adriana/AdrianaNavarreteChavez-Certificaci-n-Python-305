alumnos = ["Vanessa", "Emmanuel", "Julio", "Paola", "Rosalia"]
calificaciones = [9, 6, 10, 5, 8]

for i in range(len(alumnos)):
    nota = calificaciones[i]
    if nota >= 7:
        pass  # pendiente de guardar aprobado
    else:
        print(alumnos[i], "REQUIERE APOYO")

print("Fin")
# for 
alumnos = ["Vanessa", "Emmanuel", "Julio", "Paola", "Rosalia"]
calificaciones = [9, 6, 10, 5, 8]

i = 0
while i < len(alumnos):
    nota = calificaciones[i]
    if nota >= 7:
        pass  # pendiente de guardar aprobado
    else:
        print(alumnos[i], "REQUIERE APOYO")
    i += 1

print("Fin")
#while
#mariz 
alumnos = []
calificacion = []  # Lista para guardar las calificaciones

cantidad = int(input("¿Cuantos alumnos quieres agregar?: "))

for i in range(cantidad):
    nombre = input(f"Registra el nombre del alumno {i+1}: ")
    # Usamos una variable temporal 'nota' para evitar confundirla con la lista
    nota = int(input(f"Registra el promedio de {nombre}: "))
    
    alumnos.append(nombre)
    calificacion.append(nota)  # Agregamos la nota a la lista

print("\n--- Resultados ---")
print("Lista de alumnos:", alumnos)
print("Lista de calificaciones:", calificacion)

# Validamos que la lista no esté vacía antes de buscar
if len(calificacion) > 0:
    # Tomamos el primer elemento como base para comparar
    calificacion_alta = calificacion[0]
    calificacion_baja = calificacion[0]

    # Recorremos la lista de calificaciones para encontrar el mayor y menor
    for nota in calificacion:
        if nota > calificacion_alta:
            calificacion_alta = nota
            
        if nota < calificacion_baja:
            calificacion_baja = nota

    print(f"\nEl promedio más alto es: {calificacion_alta}")
    print(f"El promedio más bajo es: {calificacion_baja}")
else:
    print("\nNo se registraron calificaciones.")

#Matriz 
alumnos = []
calificacion = []  # Lista para guardar las calificaciones

cantidad = int(input("¿Cuantos alumnos quieres agregar?: "))

for i in range(cantidad):
    nombre = input(f"Registra el nombre del alumno {i+1}: ")
    # Usamos una variable temporal 'nota' para evitar confundirla con la lista
    nota = int(input(f"Registra el promedio de {nombre}: "))
    
    alumnos.append(nombre)
    calificacion.append(nota)  # Agregamos la nota a la lista

print("\n--- Resultados ---")
print("Lista de alumnos:", alumnos)
print("Lista de calificaciones:", calificacion)

# Validamos que la lista no esté vacía antes de buscar
if len(calificacion) > 0:
    # Tomamos el primer elemento como base para comparar
    calificacion_alta = calificacion[0]
    calificacion_baja = calificacion[0]

    # Recorremos la lista de calificaciones para encontrar el mayor y menor
    for nota in calificacion:
        if nota > calificacion_alta:
            calificacion_alta = nota
            
        if nota < calificacion_baja:
            calificacion_baja = nota

    print(f"\nEl promedio más alto es: {calificacion_alta}")
    print(f"El promedio más bajo es: {calificacion_baja}")
else:
    print("\nNo se registraron calificaciones.")

    #LEN 
    filas=len(matriz) # solo tomando esa me dice cuatas tengo cuanta los corchetes 
columnas=len(matriz[0])




#ABECEDARIO 
# 1. Creamos una lista con las letras del abecedario
abecedario = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

# 2. Vamos a acomodarlas en una matriz de filas y columnas (5 columnas por fila)
matriz_abecedario = []
columnas_deseadas = 5
fila_temporal = []

for letra in abecedario:
    fila_temporal.append(letra)
    # Cuando la fila completa 5 elementos, la guardamos en la matriz y empezamos otra
    if len(fila_temporal) == columnas_deseadas:
        matriz_abecedario.append(fila_temporal)
        fila_temporal = []

# Si sobraron letras al final (la 'Z'), agregamos esa última fila incompleta
if len(fila_temporal) > 0:
    matriz_abecedario.append(fila_temporal)

print("--- MATRIZ DEL ABECEDARIO ---")

# 3. Usamos ciclos anidados para recorrer e imprimir nuestra matriz
filas = len(matriz_abecedario)

for i in range(filas):
    # Obtenemos dinámicamente las columnas de la fila actual
    columnas = len(matriz_abecedario[i])
    
    for j in range(columnas):
        # Imprimimos cada letra con un formato bonito y sin salto de línea
        print(f"[{matriz_abecedario[i][j]}]", end=" ")
        
    # Salto de línea al terminar cada fila
    print()


    #ABECEDARIO
    # 1. Creamos la lista con las letras del abecedario
abecedario = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

matriz = []
indice_letra = 0

# 2. Llenamos la matriz usando ciclos y rangos fijos (sin len)
# Sabemos que necesitamos 6 filas para acomodar las 26 letras de 5 en 5
for i in range(6):
    fila = []
    # Cada fila tendrá 5 columnas
    for j in range(5):
        if indice_letra < 26:
            fila.append(abecedario[indice_letra])
            indice_letra += 1
        else:
            fila.append(" ") # Espacio vacío para completar la última casilla
    matriz.append(fila)

print("--- MATRIZ DEL ABECEDARIO POR ÍNDICES (SIN LEN) ---\n")

# 3. Recorremos e imprimimos la matriz usando únicamente los índices numéricos
for i in range(6):       # Rango fijo para las 6 filas
    for j in range(5):   # Rango fijo para las 5 columnas
        print(f"[{matriz[i][j]}]", end=" ")
    
    # Salto de línea al terminar cada fila
    print()



    # ESTE # HACER UNA MATRIZ EN LA CUAL SE COLOCA EL ABECEDARIO CON FILAS Y COLUMNAS
abecedario = [
    ["A", "B", "C", "D"],  # <-- ¡No olvides esta coma al final de cada fila!
    ["E", "F", "G", "H"],
    ["I", "J", "K", "L"],
    ["M", "N", "O", "P"],
    ["Q", "R", "S", "T"],
    ["U", "V", "W", "X"],
    ["Y", "Z", " ", " "]
]

# Ciclo externo para las 7 filas
for i in range(0, 7):
    # Ciclo interno para las 4 columnas (j)
    for j in range(0, 4):
        # Usamos el nombre correcto 'abecedario' en lugar de 'matriz'
        print(f"posicion[{i}][{j}]={abecedario[i][j]}")

