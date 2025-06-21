numeros=[8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Lo que sucede en este programa es que el metodo "remove" va a remover un elemento de la lista "numeros". El elemento que remueve esta determinado por la funcion "max" que, dandole una lista como parametro, va a retornar el elemento más grande de la lista, que en este caso es el número 22, por lo que "remove" va a remover "22" de la lista. Por ultimo, se muestra la lista por pantalla con el número ya removido.