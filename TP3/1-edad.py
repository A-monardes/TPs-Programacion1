# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

num = int(input("Introduzca su edad: "))
if num >= 18:
    print("Es mayor de edad")

if 65 < num >= 18:
    print("voto obligatorio")
elif 18 < num > 16 or num >= 65:
    print("no obligatorio")
else:
    print("no vota")