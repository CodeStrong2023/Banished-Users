# Ejercicio 5: Calcular el factorial de un numero mayor o igual a 0
while True:
    num = int(input("Digite un número: "))
    if num >= 0:
        break
factorial = 1
i = 1
while i <= num:
    factorial = factorial * i
    i += 1

print(f"El factorial es: {factorial}")
