import inspect

def calcular_promedio(a="primero",b="segundo",c="tercero"):
    sig=inspect.signature(calcular_promedio)
    cant=len(sig.parameters)
    prom = (a+b+c)/cant
    print(f"El promedio de los números ingresados es {prom}")


#Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

calcular_promedio(num1,num2,num3)