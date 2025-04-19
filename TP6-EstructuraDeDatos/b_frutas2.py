# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

from a_frutas import precios_frutas
import copy

precios_actualizados = copy.deepcopy(precios_frutas)

precios_actualizados['Banana'] = 1330
precios_actualizados['Manzana'] = 1700
precios_actualizados['Melón'] = 2800

if __name__ == "__main__":
    print(precios_actualizados)