# Ciclo While (mientras o durante)
"""
contador = 0
while contador < 78:
    print(f"Ejecutamos nuestro ciclo while {contador}")
    contador += 1
else:
    print("Fin del ciclo while")
"""

#Ejercicio: Imprimir números del 0 al 5 con el ciclo while
"""
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1
"""
"""
minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1
"""
"""
#Ciclo FOR
cadena = "Hello"
for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo FOR")
"""
"""
# Palabra reservada: Break
for letra in "Alemania":
    if letra == "a":
        print(f"Letra encontrada: {letra}")
        break
else:
    print("Fin del ciclo FOR")
"""

# Palabra reservada: Continue
for i in range(6):
    if i % 2 == 0:
        print(f"valor: {i}")

for i in range(6):
    if i % 2 != 0:
        continue
        print(f"valor: {i}")