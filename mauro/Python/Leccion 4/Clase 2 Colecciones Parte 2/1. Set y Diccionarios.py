# TIPO SET: coleccion de elementos sin orden y sin indice.

planetas = {"Marte", "Júpiter", "Venus"}
print(len(planetas)) # Usamos la funcion len = length = largo

# Revisar si un elemento existe dentro del set
print("Marte" in planetas)

# Agregar un elemento
planetas.add("Tierra") # Funcion add
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove("Júpiter") # Esta funcion ante un mal ingreso o inexistencia da error
print(planetas)
planetas.discard("Tierra") # Esta funcion no nos presenta ningun error si ingresamos mal el elemento
print(planetas)

# Limpiar Set
planetas.clear()
print(planetas)

# Eliminar Set o Conjunto
del planetas
#print(planetas)


# DICCIONARIO
# "Maradona":10 ----> ejemplo de diccionario, esta compuesto de dos elementos, una LLAVE y un VALOR
# dict(key,value)

diccionario = {
    "IDE" : "Integrated Develoment Environment",
    "POO" : "Programación Orientada a Objetos",
    "SABD": "Sistema de Administración de Base de Datos"
}
print(diccionario)

# Verificar la cantidad de elementos en un diccionario
print(len(diccionario))

# Acceder a un diccionario con la llave (key)
print(diccionario["IDE"])

print(diccionario.get("POO")) # Con get

# Modificamos un elemento
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Como reccorer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)

for termino, valor in diccionario.items(): # Necesitamos una funcion para recorrer un diccionario, keys y values
    print(termino, valor)

for termino in diccionario.keys(): # Funcion keys
    print(termino) # Muestra solo las llaves

for termino in diccionario.values(): # Funcion values
    print(termino) # Muestra solo los valores

# Comprobar la existencia de un elemento
print("IDE" in diccionario) # Devuelve un boolean

# Agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

# Eliminar diccionario
diccionario.pop ("SABD")
print(diccionario)

# Vaciar diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario
