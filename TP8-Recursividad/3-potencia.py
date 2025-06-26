def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base*potencia(base, exponente-1)
    
base = input("Introduci la base: ")
base = float(base)

expo = input("Introduci el exponente: ")
expo = int(expo)

resultado = potencia(base, expo)

print(f"El resultado de {base}^{expo} es: {resultado}")