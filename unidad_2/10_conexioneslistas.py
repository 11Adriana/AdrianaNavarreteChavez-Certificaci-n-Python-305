carrito=[]
cantidad=int(input("¿Cunatos productos quieres agregar al carrito?"))
for contador in range(cantidad):
    producto=input("Ingresa el producto a tu carrito")
    carrito.append(producto)
print("\nTu lista de creada correctamente")

carrito[0]="BARRITAS"
print(f"TU CARRITO CONTIENE{carrito}")
