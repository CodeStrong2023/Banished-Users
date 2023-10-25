# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos, por último mostrar la lista.

lista = [1, 2, 3, "Mauro", 4, 4, 5, 6, 7, 7, 3, 8, "Juan", 5, "Mauro"]
# conjunto = set(lista) # Se convierte la lista a un set
# print(conjunto)
# lista = list(conjunto) # Se convierte el set a list
lista = list(set(lista)) # Conversion en una sola linea
print(lista)