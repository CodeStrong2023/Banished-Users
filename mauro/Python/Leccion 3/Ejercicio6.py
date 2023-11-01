"""
    Ejercicio 7: Ingresar "N" enteros, visualizar la suma 
    de los numeros pares de la lista, cuantos numeros pares
    existen y cual es el promedio de los numeros impares
"""
n_elementos = int(input("Digite la cantidad de elementos a ingresar: "))

i = 1
suma_pares = 0
conteo_pares = 0
suma_impares = 0
conteo_impares = 0
while i <= n_elementos:
    num = int(input("Digite un número: "))
    if num % 2 == 0:
        suma_pares += num
        conteo_pares += 1
    else:
        suma_impares += num
        conteo_impares += 1
    i += 1

if conteo_pares == 0:
    print("No se han digitado números pares")
else:
    print(f"La suma de los números pares es: {suma_pares}")
    print(f"El conteo de los números pares es: {conteo_pares}")

if conteo_impares == 0:
    print("No se han digitado números impares")
else:
    promedio_impares = suma_impares/conteo_impares
    print(f"El promedio de los numeros impares es: {promedio_impares}")