# Ejercicio 4
import math # Importamos la clase math para hacer uso de funciones como sqrt (raiz cuadrada)

# Sacar raiz cuadrada de un número positivo
num = int(input("Digite un número positivo: "))

while num < 0:
    print("El num debe ser positivo")
    num = int(input("Digite un número positivo: "))
print(f"La raiz cuadrada es {num} es {math.sqrt(num):.2f}")