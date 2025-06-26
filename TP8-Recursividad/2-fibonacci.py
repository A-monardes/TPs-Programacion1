def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
posicion=input("Introduzca la posición maxima que quiera ver (no negativo): ")
posicion=int(posicion)

print(f"Fibonacci hasta la posicion {posicion}: ")
serie=[]

for i in range(posicion+1):
    valor_fibo=fibonacci(i)
    serie.append(valor_fibo)

print(serie)