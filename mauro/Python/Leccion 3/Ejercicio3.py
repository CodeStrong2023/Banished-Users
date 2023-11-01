"""
Ejercicio 3: Leer 10 numeros e imprimir cuantos positivos
cuantos negativos y cuantos neutros
"""
positivos = 0
negativos = 0
neutros = 0
for i in range(1,10):
    num = int(input("Digite un número: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        neutros += 1

print(f"Cantidad de positivos: {positivos}")
print(f"Cantidad de negativos: {negativos}")
print(f"Cantidad de neutros: {neutros}")
