#cadenas y concatenacio con (+)
cadena1='HOLA '
cadena2="MUNDO "
multilinea=""" ESTO ES UNA CADENA
DE VARIAS LIENAS"""
#UNA DE LAS FORMAS MAS FACILES ES CON SIGNO +
print(cadena1 + cadena2 + multilinea)
#CADENAS Y REPETICION 
eco="JA"*3
print(eco)
#CAMBIAR UNA CADENAS DE MINUSCULA A MAYUSCULA
tu_nombre='Adriana'
print(tu_nombre.upper())
#CAMBIAR CADENA DE MAYUSCULA A MINISCULA 
print(tu_nombre.lower())
#REMPLAZAR TEXTO EN UNA CADENA 
frase="Me gusta Programacion"
print(frase.replace("Me gusta Programacion","Matematicas"))
#FORMATO CADENAS (F-String)
edad=23
nombre='Adriana'
mensaje=f"Hola me llamo {nombre} y tengo {edad}años"
print(mensaje)
#CONTAR LOS CARACTERES DE CADA DE UNA PADENA 
texto= "Felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#COMPROBAR SI UN TEXTO TIENE UNA PALABRA 
oracion="APRENDER PYTHON ES DIVERTIDO"
if "WITTO" in oracion:
    print("ENCONTRADO")
else:
    print("NO ESTA ")
# VALIDDAR EL CONTENIDO DE UNA CADENA
nlista="WITTO"
print(nlista.isalpha())#cotejar si son letras y debuelve valor boleano
print(nlista.isdigit())#COTEJAR SI SI TIENE NUMEROS 
nlista="23"
print(nlista.isalpha())#cotejar si son letras y debuelve valor boleano
print(nlista.isdigit())#COTEJAR SI SI TIENE NUMEROS 
 
