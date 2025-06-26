def facto(n):
    if n<=1:
        return 1
    else:
        return n * facto(n-1)
    
num=input("Introduzca el número: ")
num=int(num)

for i in range (1, num+1):
    result=facto(i)
    print(f"El factorial de {i} es {result}")