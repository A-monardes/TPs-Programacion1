def es_palindromo(palabra):
    if len(palabra)<=1:
        return True
    
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False
    
entrada = input("Introduci una palara (sin espacio ni tildes): ")
es = es_palindromo(entrada)

print(f"{entrada} {'es' if es else 'no es'} un palíndromo.")