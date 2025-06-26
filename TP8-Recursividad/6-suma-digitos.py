def suma_digitos(n):
    if n<10:
        return n
    else:
        return (n%10)+suma_digitos(n//10)

entrada = input("Introduzca un número entero no negativo: ")
num = int(entrada)

resultado = suma_digitos(num)
print(f"La suma de los dígitos de {num} es: {resultado}")