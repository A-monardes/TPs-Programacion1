#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

rango=100
sum=0
for x in range (rango):
    num = int(input(f"({x+1}) Ingrese un número: "))
    sum+=num

print(f"La media de los números ingresados es {(sum/rango)}")