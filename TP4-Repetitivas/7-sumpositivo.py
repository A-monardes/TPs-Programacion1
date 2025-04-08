#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num = int(input("Ingrese un número positivo: "))
sum=0

if num > 0:
    for x in range (num):
        sum+=x
    print(f"La suma de los números entre 0 y {num} es {sum}")
else:
    print("Por favor, ingrese un número positivo.")