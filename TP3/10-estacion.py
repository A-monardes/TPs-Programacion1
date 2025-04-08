# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

# Periodo del año               Estación en el hemisferio norte               Estación en el hemisferio sur

# Desde el 21 de diciembre 
# hasta el 20 de 
# marzo (incluidos)             Invierno                                      Verano

# Desde el 21 de marzo 
# hasta el 20 de junio
# (incluidos)                   Primavera                                     Otoño

# Desde el 21 de junio
# hasta el 20 de
# septiembre
# (incluidos)                   Verano                                        Invierno

# Desde el 21 de septiembre
# hasta el 20 de diciembre
# (incluidos)                   Otoño                                         Primavera


# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese en que hemisferio se encuentra (N/S): ").upper()
mes = int(input("Ingrese en que mes se encuentra (1 al 12): "))
dia = int(input("Ingrese en que dia se encuentra (1 al 31): "))

if (hemisferio == "N" and ((mes==12 and dia>=21) or (mes==1) or (mes==2) or (mes==3 and dia<=20))) or (hemisferio == "S" and ((mes==6 and dia>=21) or (mes==7) or (mes==8) or (mes==9 and dia<=20))):
    print(f"Hoy es {dia}/{mes} en el hemisferio {hemisferio}, es invierno")
elif (hemisferio == "N" and ((mes==3 and dia>=21) or (mes==4) or (mes==5) or (mes==6 and dia<=20))) or (hemisferio == "S" and ((mes==9 and dia>=21) or (mes==10) or (mes==11) or (mes==12 and dia<=20))):
    print(f"Hoy es {dia}/{mes} en el hemisferio {hemisferio}, es primavera")
elif (hemisferio == "N" and ((mes==6 and dia>=21) or (mes==7) or (mes==8) or (mes==9 and dia<=20))) or (hemisferio == "S" and ((mes==12 and dia>=21) or (mes==1) or (mes==2) or (mes==3 and dia<=20))):
    print(f"Hoy es {dia}/{mes} en el hemisferio {hemisferio}, es verano")
elif (hemisferio == "N" and ((mes==9 and dia>=21) or (mes==10) or (mes==11) or (mes==12 and dia<=20))) or (hemisferio == "S" and ((mes==3 and dia>=21) or (mes==4) or (mes==5) or (mes==6 and dia<=20))):
    print(f"Hoy es {dia}/{mes} en el hemisferio {hemisferio}, es otoño")