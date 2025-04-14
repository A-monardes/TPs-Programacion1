def segundos_a_horas(segundos):
    horas = segundos/3600
    print(f"{segundos} segundos son {round(horas,2)} horas")

#Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

segundos = int(input("Ingrese los segundos: "))
segundos_a_horas(segundos)