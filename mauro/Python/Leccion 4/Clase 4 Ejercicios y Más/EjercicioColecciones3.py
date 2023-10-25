# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon, Clase: Guerrero, Raza: Dúnadan del norte
# Nombre: Gandalf, Clase: Mago, Raza: Istar
# Nombre: Legolas, Clase: Arquero, Raza: Elfo Sindar

pjs = [] # Lista vacia
# Diccionario
p1 = {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dúnadan del Norte"},
pjs.append(p1) # Se agregan a la lista vacia
p2 = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"},
pjs.append(p2)
p3 = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"},
pjs.append(p3)
# Agregar 3 pjs mas
p4 = {"Nombre": "Arwen", "Clase": "Hechicera", "Raza": "Medio elfo"},
pjs.append(p4)
p5 = {"Nombre": "Gimli", "Clase": "Guerrero Enano", "Raza": "Enano de las Montañas"},
pjs.append(p5)
p6 = {"Nombre": "Frodo Bolsón", "Clase": "Portador del Anillo", "Raza": "Hobbit"},
pjs.append(p6)

print(pjs)  