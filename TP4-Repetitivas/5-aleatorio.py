#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

x=random.randint(0,9)
num = int(input("Ingrese un número entre 0 y 9: "))
while num != x:
    num = int(input("Número incorrecto. Intentelo con otro número: "))
print("¡Correcto! El número es ", x)