def informacion_personal(n,a,e,r):
    print(f"Soy {n} {a}, tengo {e} años y vivo en {r}")

#Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu residencia: ")

informacion_personal(nombre,apellido,edad,residencia)