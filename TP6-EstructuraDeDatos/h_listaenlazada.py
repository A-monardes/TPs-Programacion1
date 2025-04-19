# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar los valores almacenados.

class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.sig=None

class Lista:
    def __init__(self):
        self.comienzo=None

    def insertar(self, dato):
        nuevo_nodo= Nodo(dato)
        nuevo_nodo.sig=self.comienzo
        self.comienzo=nuevo_nodo

    def imprimir(self):
        actual=self.comienzo
        while actual:
            print(actual.dato, end=' --> ')
            actual=actual.sig
        print("Fin")

lista = Lista()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)
lista.imprimir()