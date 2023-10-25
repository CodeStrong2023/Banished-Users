# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los número del 1 al 10, luego modificar los
# elementos de la lista multiplicandolos por un valor ingresado por el usuarios.

lista = list(range(1,11))
print("Lista Original")
for i in lista:
    print(i, end="-")

valor = int(input("\n Digite un valor a multiplicar: "))

# Se multiplican los valores de la lista
for indice, i in enumerate(lista): # Funcion para modificar los indices de la lista
    lista[indice] *= valor  # El iterador solo recorre los indices, en esta linea se multiplica

print(f"Lista final con los elementos multiplicados por {valor}")
for i in lista:
    print(i, end="-")