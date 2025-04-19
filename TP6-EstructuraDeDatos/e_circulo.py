# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
# Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋.
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi*(self.radio**2)
        print(f"El area del circulo con radio {self.radio} es de {area:.2f}")
    
    def calcular_perimetro(self):
        perimetro = 2*math.pi*self.radio
        print(f"El perimetro del circulo con radio {self.radio} es de {perimetro:.2f}")

radio1 = float(input("Introduzca el radio del circulo: "))

circulo1 = Circulo(radio1)

circulo1.calcular_area()
circulo1.calcular_perimetro()