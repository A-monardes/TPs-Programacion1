def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    mult=a*b
    div=a/b
    resultado = (suma,resta,mult,div)
    return resultado

#Crear una función llamada operaciones_basicas(a, b) que recibados números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resul = operaciones_basicas(num1,num2)

print(f" La suma de {num1} y {num2} es {resul[0]} \n La resta de {num1} y {num2} es {resul[1]} \n El producto de {num1} multipicado por {num2} es {resul[2]} \n El cociente de {num1} dividido {num2} es {resul[3]}")