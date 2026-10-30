dias_permitidos=("lunes","miercoles","viernes")
dia_solicitado= input("introduce el dia que quieres solicitar:")
if dia_solicitado in dias_permitidos:
    print(f"El dia introduccido {dia_solicitado} si hay servicio")
else:
    
    print(f"No hay atención ese día {dia_solicitado}. Solo se atiende lunes, miércoles y viernes.")