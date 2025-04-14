import math

def calcular_area_circulo(radio):
    area = math.pi*(radio**2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2*math.pi*radio
    return perimetro
    
#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

radio = input("Ingrese el radio del circulo: ")
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es de {area} y el perimetro es {perimetro}")