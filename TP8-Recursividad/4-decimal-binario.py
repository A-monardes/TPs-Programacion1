def decimal_a_binario(num_decimal):
    if num_decimal==0:
        return "0"
    elif num_decimal==1:
        return "1"
    else:
        return decimal_a_binario(num_decimal//2)+str(num_decimal%2)


decimal = input("Introduzca un número decimal entero (no negativo): ") 
decimal = int(decimal)

binario=decimal_a_binario(decimal)

print(f"El número {decimal} en binario es {binario}")