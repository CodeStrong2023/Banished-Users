# Desempaquetado de Listas o List Unpacking
def show(name, lastName):
    print(name+' '+lastName)

person = ['Mauro', 'Mesas']
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la función
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto

person2 = ('Carlos', 'Montana') # Desempaquetamos a traves de una tupla
show(*person2)
person3 = {'lastName': 'Mesas', 'name': 'Mauro'}
show(**person3)


# List Comprehension o Lista de compresión: tomar solo lo necesario de la lista sin hacer modificaciones
names = ['Paolo', 'Rodrigo', 'Lupe', 'Pepe']

alongP = [p for p in names if p[0] == 'P'] # Esto regresa una nueva lista
print (alongP)

# Con Diccionarios
bottleC = [{'name': 'Quilmes', 'country': 'Arg'},
           {'name': 'Corona', 'country': 'Mx'},
           {'name': 'Stella Artois', 'country': 'Belgium'},
           ]
Arg = [b for b in bottleC if b['country'] == 'Arg']
print(Arg)
print(bottleC)