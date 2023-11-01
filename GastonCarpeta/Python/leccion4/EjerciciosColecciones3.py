# ejercicio 3: agregar personajes a una lista
#escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
#nombre: aragon
#clase: guerrero
#raza: dunadan del norte

#nombre: gandalf
#clase: mago
#raza: istar

#nombre: legolas
#clase: arquero
#raza: elfo sindar

personajes = [] # creamos una lista vacia
#creamos diccionarios
P = {'nombre': 'aragon', 'clase': 'guerrero', 'raza': 'dunadan del norte'}
personajes.append(P) #agregamos a la lista un personaje
P = {'nombre': 'gandalf', 'clase': 'mago', 'raza': 'istar'}
personajes.append(P)
P = {'nombre': 'legolas', 'clase': 'arquero', 'raza': 'elfo sindar'}
personajes.append(P)
print(personajes)
# tarea agregar 3 personajes que sean a tu eleccion
P = {'nombre': 'frodo', 'clase': 'portador de anillos', 'raza': 'hobbits'}
personajes.append(P)
P = {'nombre': 'gollum', 'clase': 'mounstro', 'raza': 'hobbit bipolar'}
personajes.append(P)
P = {'nombre': 'sauron', 'clase': 'ainur', 'raza': 'ainur maiar'}
personajes.append(P)