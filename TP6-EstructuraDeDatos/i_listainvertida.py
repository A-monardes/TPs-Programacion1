# 9) Dada una lista enlazada, implementa una función para invertirla.

import h_listaenlazada

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

    def invertir(self):
        anterior = None
        actual = self.comienzo
        while actual:
            siguiente = actual.sig
            actual.sig = anterior
            anterior = actual
            actual = siguiente
        self.comienzo=anterior
    

lista = Lista()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)

lista.invertir()
lista.imprimir()