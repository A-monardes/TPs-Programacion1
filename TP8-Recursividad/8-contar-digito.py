def contar_digito(numero, digito):
    if numero==0:
        return 1 if digito==0 else 0
    
    if numero<10:
        return 1 if numero==digito else 0
    
    ultimo=numero%10

    conteo = 1 if ultimo == digito else 0

    return conteo + contar_digito(numero//10, digito)

num = input("Introduci un número entero no negativo: ")
num = int(num)

digito = input("Introduci el digito a buscar (0-9): ")
digito = int(digito)

conteo=contar_digito(num, digito)

print(f"El dígito {digito} aparece {conteo} veces en el número {num}.")