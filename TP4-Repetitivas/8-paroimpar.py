#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

par=0
impar=0

for x in range (100):
    num=int(input(f"({x+1})Ingrese un número: "))
    if num%2==0:
        par+=1
    else:
        impar+=1
print(f"De los números ingresados, {par} son par y {impar} son impar")