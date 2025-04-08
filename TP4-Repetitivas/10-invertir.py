    #10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número: "))
inver=0
x=num

while num > 0:
    digi=num%10
    inver=(inver*10)+digi
    num=num//10

print(f"El número {x} invertido es {inver}")