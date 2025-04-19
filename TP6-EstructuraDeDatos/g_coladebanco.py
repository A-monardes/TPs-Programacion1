# 7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
# ● Agregar clientes (encolar).
# ● Atender clientes (desencolar).
# ● Mostrar el siguiente cliente en la fila.
from collections import deque

class Cola:
    def __init__(self):
        self.x = deque()

    def encolar(self, x):
        self.x.append(x)
    
    def vacia(self):
        return len(self.x) == 0

    def desencolar(self):
        return self.x.popleft() if not self.vacia() else "La cola esta vacia"
    
    def siguiente(self):
        return self.x[0] if not self.vacia() else "La cola esta vacia"
    
cola = Cola()

cola.encolar("🎫 1")    
cola.encolar("🎫 2")    
cola.encolar("🎫 3")

for x in range (len(cola.x)):
    print(f"Turno actual: {cola.desencolar()}")
    print(f"El siguiente es : {cola.siguiente()}")