# Pilas usando listas
pila = [1, 2, 3]

# Agregamos elementos la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos del final
elementoBorrado = pila.pop() # Quita el ultimo elemento y lo guarda en la variable
print(f"Sacamos el elemento {elementoBorrado}")
print(f"La pila ahora queda: {pila}")


# Colas con listas
# Estructura de datos tipo "fifo" (first input / first output)
cola = ["Juan", "Marcos", "Rodrigo", "Liliana"]

# Agregamos elementos al final de la cola
cola.append("Natalia")
cola.append("Jose")
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f"Atendido: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido: {seRetira}")
print(cola)