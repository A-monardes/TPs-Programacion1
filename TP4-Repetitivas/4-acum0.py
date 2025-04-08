#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

num = int(input("Ingrese un número entero: "))
sum=0

while num !=0:
    sum+=num
    num = int(input("Ingrese otro número o ingrese 0 para salir: "))
print("La suma de todos los números ingresados es ", sum)