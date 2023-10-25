# LISTAS = estructura de datos que se utiliza para almacenar una colección ordenada de elementos

# Lista = Mauro, Lorena, Agustin, Ariel
#           0       1       2       3
nombres = [ "Mauro","Lorena","Agustin","Ariel" ]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[-1]) # Uso de negativo para imprimir el ultimo.
print(nombres[-2])

print(nombres[0:2]) # Solo muestra el indice 0 y 1, pero no el indice 2

# Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # Indices a mostrar 0 , 1 , 2

# Ir desde el indice indicado hasta el final
print(nombres[1: ])

# Modificamos un valor
nombres[3] = "Juan"
nombres[0] = "Osvaldo"
print(nombres)

# Iterar una lista
for nombre in nombres: # Nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

# Agregamos un elemento con el operador "."
nombres.append("Marcelo")
#nombres.append(1,2,3)
#nombres.append(True)
#nombres.append(10,45)
# Pueden haber elementos float, boolean, int, etc
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, "Alberto")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

# Eliminamos un elemento de la lista
nombres.remove("Alberto")
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2]
print(nombres)

# Eliminal, borrar, limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
#print(nombres)



# TUPLAS = Son como las listas pero inmutables

# Definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)
print (len(cocina))

# Acceder a un elemento (para esto usamos corchetes no parentesis)
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ("papa",) # Una tupla necesita aunque sea un elemento la coma, de lo contrario seria un string, cadena

# Recorremos los elementos de la tupla
for cocinar in cocina: # Print esta usando /n para saltos de linea
    print(cocinar, end=" ")  # Usamos End = para eliminar los saltos de lineas

# Modificar una tupla, no se debe hacer a menos que no halla otra opción
    # se debe convertir la tupla en lista y nuevamente a tupla
cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("\n",cocina)

# del cocina ... esto es para eliminar una tupla
