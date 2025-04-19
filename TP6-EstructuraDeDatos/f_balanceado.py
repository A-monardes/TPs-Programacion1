# 6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente balanceados usando una pila.
 
def balanceado (x):
    pila=[]
    diccionario= {')':'(','}':'{',']':'['}
    
    for char in x:
        if char in diccionario.values():
            pila.append(char)
        elif char in diccionario.keys():
            if pila.pop() != diccionario[char]:
                return False
    return not pila

print(balanceado("({[]})"))
print(balanceado("({[})"))