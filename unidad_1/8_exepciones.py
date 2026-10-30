try:
    numero1=int(input("Ingresa el primer numero:"))
    numero2=int(input("Ingresa el segundo numero:"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("DIVISION ENTRE CERO FALLIDA")
except ValueError:
    print("SOLO SE ACEPTAN NUMEROS ")
else:
    print("El resultado es: ",resultado)
finally:
    print("Programa finalizado")