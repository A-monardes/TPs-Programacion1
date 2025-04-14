def celsius_a_fahrenheit(c):
    f=((9/5)*c)+32
    print(f"La temperatura {c}C° es equivalente a {f}F°")

#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

num = float(input("Ingrese la temperatura en Celsius: "))
celsius_a_fahrenheit(num)