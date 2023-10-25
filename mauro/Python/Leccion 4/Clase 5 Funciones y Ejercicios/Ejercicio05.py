# Ejercicio 2: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo

numero = int(input("Digite un número positivo: "))
while numero < 0:
    print("Error! El numero tiene que ser positivo")
    numero = int(input("Digite un número positivo: "))
factorial = 1
for i in range(1, numero+1):
    factorial *= i
print(f"El factorial del numero {numero} es {factorial}")