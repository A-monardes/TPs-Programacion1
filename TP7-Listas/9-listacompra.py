compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print(f"Lista original: {compras}")

compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")

print(f"Lista modificada {compras}")