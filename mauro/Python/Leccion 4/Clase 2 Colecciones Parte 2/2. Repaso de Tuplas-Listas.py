# Listas (mas conceptos)

# Concatenar Listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) # Funcion para agregar varios elementos a la lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado
#print(lista3.index(0)) # Da error por no ser parte de la lista

print(lista3.count(1)) # Funcion para saber cuantos valores repetidos hay dentro de una lista

lista3.reverse() # Funcion para poner una lista al reves
print(lista3)

# Multiplicar elementos de la lista
Lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento
lista3.sort() # Funcion para ordenar lista de forma ascendentemente
print(lista3)
lista3.sort(reverse=True) # decendentemente
print(lista3)


# Tuplas (mas conceptos)

tupla = (4, "Hola", 6.68, [5, 10, 20], 4, "Chau") # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo boolean
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tuplas a listas y listas a tuplas