#Creando un diccionario con python 
persona={
    "nombre":"Witto Gonzalez",
    "edad":22,
    "profesion":"piloto ",
    "estudiante": True

}
print(persona)
#accediendo a un valor en espeecifico
print(persona["nombre"])
#se puede usar el metodo GET
# es util porque no me da error si la clave existe 
print(persona.get("edad"))
#identificar un valor existente 
persona["edad"]=23
print(persona.get("edad"))
#agregar un par (calve:valor)
persona["ciudad"]="Monterrey"
print(persona)
#recorrer un diccionario 
for clave,valor in persona.items():
    print(f"{clave}:{valor}")
