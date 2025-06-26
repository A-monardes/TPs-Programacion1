def contar_bloques(n):
    if n==1:
        return 1
    else:
        return n+contar_bloques(n-1)

entrada=input("Introduzca el número de bloques para la base de la piramidae (entero no negativo): ")
num=int(entrada)

total=contar_bloques(num)

print(f"Para una píramide con {num} bloques en la base, se necesitan un total de {total} bloques.")