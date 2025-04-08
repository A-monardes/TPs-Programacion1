#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
sum=0

for x in range (n1+1,n2):
    sum+=x
print(f"La suma de los números entre {n1} y {n2} es {sum}")