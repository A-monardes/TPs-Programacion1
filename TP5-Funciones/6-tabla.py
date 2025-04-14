def tabla_multiplicar(num):
    for x in range (1,11):
        print(f"{num}x{x}= {num*x}")

#Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

num = int(input("Ingrese un número: "))
tabla_multiplicar(num)