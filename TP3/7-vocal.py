# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase = input("Ingrese una frase ").lower()

frase_largo = len(frase)

final = frase[frase_largo - 1]

if final=="a" or final=="e" or final=="i" or final=="o" or final=="u":
    print(frase+"!")
else:
    print(frase)