# Lista  = conjunto de elementos puedo tener nombres numeros
#coleccion en python

# las listas es lo que se conoce en otros leguajes como arreglos o vectores
nombre = ['naty', 'osvaldo', 'lili', 'luquita', 'alberto']
"""
print(nombre)
print(nombre[0])
print(nombre[1])
"""
"""
# como recuperar un rango de la lista
print(nombre)
print(nombre[0:2])# solo muestra el indice 0 y 1 el 2 no lo muestra
# ir del inicio de la lista al indice (sin incluirlo)
#print(nombre[_:3])_#indice a mostrar 0,1,2
#desde el indice indicado hasta el final
print(nombre[1: ])
#modificaremos un valor
nombre[2] = 'liliana'
nombre[0] = 'natalia'
print(nombre)
#iterar una lista
for nombre in nombre: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('se acabaron los elementos de la lista')
    # preguntamos cuantos elementos tiene
print(len((nombre))) # le pasamos como parametros la lista

#agregamos un elemento
nombre.append('marcelo')
nombres.append('marcelo')
nombres.append([1,2,3])
nombres.append(True)
nombre.append(10.45)
nombre.append([4,5])
nombres.append([7])
print(nombre)


# insertar un elemento en el indice especifico
nombre.insert(1,'alberto')
print(nombre)
nombre.insert(3,'debora')
print(nombre)

#eliminemos un elemento
nombre.remove('alberto')
print(nombre)

# eliminar el ultimo elemento
nombre.pop()
print(nombre)

#eliminar un indice especifico
del nombre[2] # del significa delete (eliminar)
print(nombre)

#eliminar, borrar o limpiar todos los elementos
nombre.clear()
print(nombre)

#eliminar lista
del nombre
print(nombre) # aca mostramos un error 
"""
"""
sintaxis de rango(inicio<opcional>, fin <requerido>, incremento <opcional>)



"""
"""
#ejercicio 1: iterar un rango de 0 a 10 e imprementar numeros divisibles entre 3
#ejemplo de ejecucion: 0,3,6,9
print('rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

#ejercicio 2: crear un rango de numeros de 2 a 6 a imprimelos
#ejemplo de ejecucion: 2,3,4,5,5
print('rango con valores de inicio = 2 y fin = 6')
rango = range(2, 7)
for i in rango:
    print(i)

#ejercicio de 3: crear un angulo de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
#ejemplo de ejecucuion: 3,5,7,9
print('rango con valores de inicio = 3, fin= 10, incremento = 2')
for i in range(3,11,2):
    print(i)
"""
"""
# definimos una tupla
cocina = ('cuchara' , 'cuchillo', 'tenedor')
print(len)cocina))

# acceder a un elemento, para  esto utilizamos corchetes no parentesis
print(cocina[0])
#mostrar de manera inversa
print(cocina[-1])

# acceder a un rango
print(cocina[0:1])
#ejemplo
verduras = ('papa',) # una tupla necesita aunque sea de un elemento: la coma
#de lo contrario solo seria un tipo de str cadena

#recorremos los elementos de la tupla
for cocinar in cocina:_# print esta usando /n para saltos de lineas
    print(cocinar, end=' ')_#usamos end= para eliminar los saltos de linea

cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tupl(cocinaLista)
print('\n', cocina)

#del cocina # esto es para eliminar una tupla
""""""
# Tipo set
planetas = {'marte', 'jupiter', 'venus'}
print(len(planetas)) #usamos la funcion len = length significa largo

#revisar si un elemento existe dentro de set
print('jupiter' in planetas)

#agregar un elemento
planetas.add('tierra') # add es una funcion
print(planetas)

#eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('jupiter')# esta funcion ante un mal ingreso u enexistente del elemento da error
print(planetas)
planetas.discard('tierra')# esta funcion no nos presenta ningun error
print(planetas)

#limpiar set
planetas.clear()
print(plantas)

#eliminar set o conjunto
del planetas
#print(planetas) #al eliminar nos muestra un error


# 'Maradona':10 un diccionario esta compuesto por dos elementos
#UNA LLAVE Y UN VALOR
#dict(key,value)"""
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistemas de Administracion de Base de Datos'
}
# verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# como recorrer los elementos
for termino in diccionario:#recorremos mostrando solo las llaves
    print(termino)

#necesitamos una funcion para recorrer
for termino, valor in diccionario.items():
    print(termino, valor )

# otras maneras de acceder a un diccionario
for termino in diccionario.keys():#estamos usando una funcion
    print(termino) #muestra solo las llaves


for valor in diccionario.values(): # usamos una funcion para acceder al valor
    print(valor)

#comprobar la existencia de algun elemento
print('IDE' in diccionario) # devuelve un booleano

#agregar un elemento
diccionario['PK'] = 'primary key'
print(diccionario)

#eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#como vaciar un diccionario
diccionario.clear()
print(diccionario)

#eliminar diccionario
del diccionario# el diccionario se borro
#concatenamos listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1+lista2 # concatenamos
print(lista3)

lista3.extend([7,8,9,1]) #funcion para agreggar varios elementos a una lista
print(lista3)

print(lista3.index(5)) #funcion para ubicar en que indice esta el valor ingresado
print(lista3.index(1)) # esto daria un error por no ser el elemento parte de la lista


# como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # cuenta cuantos valores iguales hay dentro de una lista

# para poner al reves una lista
lista3.reverse()
print(lista3)

# para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# metodos de ordenamiento
lista3.sort() # ordena los elementos de forma ascendente
print(lista3)
lista3.sort(reverse=True) #ordena los elementos de forma descendente
print(lista3)

#repaso de tuplas
tupla = (4, 'hola' , 6.78, [1,2,78],4, 'hola') # puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # accion booleana, su respuesta es de tipo booleana
#lo que podemos usar dentro de tuplas son: index, count, len
# en tuplas se puede convertir de tupla a lista y de lista a tupla

#repaso de set o conjunto
#para definir un conjunto
conjunto = set()
conjunto1 = {'bye',}
conjunto.add(7)
conjunto.add('Hola')
print(conjunto)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) #Preguntamos si el numero 3 NO esta esta en el conjunto1


# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto) # nos devuelve como respuesta un booleano

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # la linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # asigna el valor que esta en el conjunto1 i no en el conjunto2
print(conjunto3)
conjunto3 = conjunto - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elementos que no comparte o que son diferentes entre ambo
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # aqui preguntamos si un conjunto es un subconjunto
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issubset(conjunto1)) # preguntamos si los elementos del conjunto1 estan en el otro conjunto del 3
print(conjunto3.issubset(conjunto2))# si es verdadero quiere decir que el conjunto es un sub conjunto
print(conjunto2.issubset(conjunto3))

# como saber si ambos conjuntos son disconexo, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # no hay cosas en comun

# convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # esto hace que el conjunto sea totalmente inmutable
# no se puede agregar, modofocar ni eliminar elementos del conjunto

# repaso diccionarios
diccionarioNuevo = {'Azul' : 'Blue' , 'Rojo' : 'Red' , 'verde' : 'green' , 'amarillo' : 'Yellow'}
print(diccionarioNuevo)

#como eliminar
del (diccionarioNuevo['Azul']) #en un diccionario aceptan distintos tipos de datos
print(diccionarioNuevo)

# los diccionarios pueden almacenar diferentes tipos de datos (las listas van con []
diccionario2 = {'ariel' : {'Edad' : 40, 'Altur' : 1.83}, 'Osvaldo' : [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)
seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones' , 'Posicion': 'Extremo Derecho'},
    11: {'nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millons', 'posicion': 'Extremo Derecho'},
    24: {'nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millons', 'posicion': 'Media Punta'},
    19: {'nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millons', 'posicion': 'Defensa central'},
    1: {'nombre': 'franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millons', 'posicion': 'portero'},
    23:{'nombre':'Emiliano Martinez' , 'Edad': 31, 'Altura': 1.90 , 'Precio': '28Millones', 'posicion': ' Arquero'},
    9:{'nombre':'Julian Alvarez ' , 'Edad': 23, 'Altura': 1.77, 'Precio': '60Millones', 'posicion': 'delantero centro'},
    22:{'nombre':'lautaro martinez' , 'Edad': 26, 'Altura': 1.78, 'Precio':'85Millones', 'posicion': 'delantero centro '},
    16:{'nombre':'Angel correa' , 'Edad': 28, 'Altura': 1.80, 'Precio': '30Millones', 'posicion': ' extremo derecho'},
    20:{'nombre':'alexis mac allister' , 'Edad': 24, 'Altura':1.79 , 'Precio': '65Millones', 'posicion': 'medio centro '},
 }
print(seleccionArgentina[10])

for llave, valor in seleccionArgentina.values():
    print(llave, valor)

# como tarea agregar por lo menos 4 jugadores mas al diccionario: seleccionArgentina
print('tenemos cargado en el diccionario la cantidad de jugadores: ', end='')
print(len(seleccionArgentina))

# pilas usando listas
pila = [1,2,3]

# agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# sacamos elementos desde el final
elementoBorrado = pila.pop()# quita el ultimo elemento y lo guarda en la variable
print(f'sacamos el elemento: {elementoBorrado}')
print(f'la pila ahora quedo asi: {pila}')

# colas con listas
# estructuras de datos de tipo fifo ( first input / first output) significa primero en salir, ultimo en entrar
cola = ['ariel', 'osvaldo', 'liliana', 'pilar']
# Agregamos elementos al final de la cola
cola.append('natalia')
cola.append('jose')
print(cola)

# sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

# seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')

