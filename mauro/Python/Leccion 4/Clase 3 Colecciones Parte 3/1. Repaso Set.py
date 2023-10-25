# Repaso de Set o Conjunto

# Para definir un conjunto
conjunto2 = set()
conjunto1 = {"wey", } # Tiene que tener un elemento y terminal con , para inicializarlo
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1) # Se pregunta si el num 3 NO esta en el conjunto

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuelve un boolean

# Operaciones en conjunto
conjunto3 = conjunto1 | conjunto2 # La linea concatena a los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Elemento que tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2  # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2   # Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Preguntamos si un conjunto es subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan en el conjunto3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # No hay elementos en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset 