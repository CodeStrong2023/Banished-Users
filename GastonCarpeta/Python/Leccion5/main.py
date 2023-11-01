# comenzamos con funciones
#mi_funcion() # no se puede llamar antes de definir a una funcion
# definimos una funcion
def mi_funcion(): # para identificar a la funcion utilizamos parentesis
    print('saludos a todos los alumnos de la tecnicatura')

mi_funcion() #estamos llamando a la funcion
mi_funcion() # se puede llamar a una funcion N cantidad de veces

# comenzamos con funciones
#mi funcion() no se puede llamar antes de definir a una funcion
#definimos una funcion
def mi_funcion(): #para identificar a la funcion utilizamos parentesis
    print('saludos a todos los alumnos de la tecnicatura')

mi_funcion() # estamos llamando a la funcion
mi_funcion()# se puede llamar a una funcion N cantidad de veces
#desempaquetado de listas o list unpacking
def show(name, lastName,)
person = ["ariel" , "betancud"]
show(persona[0], persona[1]) # pasamos uno por uno los datos de la lista a la funcion
persona2 = ("osvaldo" , "giordanini")# desempaquetamos a traves de una tupla
show(persona2)
persona3 = {"lastName": "lucero", "name": "natalia"}
show(**persona3)

numbers = [1,2,3,4,5] # aun con la ñista vacia se va a ejecutar el else
for n in numbers:
    print(numbers)
    if n == 3:
        break # esta es la unica manera para que no se ejecuta el else
else:
    print('esto se termino'

#list comprhension, lista de comprension
names = ["paolo" "rodrigo", "lupe", "pepe"]
alongP = [p for p in names if p[0] == 'p'] # esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "quiles" , "conuntry": "Arg"},
           {"name": "corona", "country": " belgium"}
           ]
Arg = [b for b in bottleC if b ["country"]== "Arg"]
print(Arg)
print(bottleC)

# paso de argumentos (funciones)
def mi_funcion2(name, lastName)
    print("saludos a todos lo que ven a traves del canal de youtube")
    print(f'nombre: {name}, apellido: {lastName}')
mi_funcion2('jorge','lucero')
mi_funcion2('ariel', 'betancud')
mi_funcion2('analia','pedrosa')

# la palabra return en funciones
# creamos una funcion para sumar
def sumar(a,b):
    return a + b
#resultado = sumar(78, 22)
#print(f'el resultado de la suma es: {resultado}')
print(f'resultado de la suma es: {sumar(55, 45)}')

def sumar2(a:int= 0, b:int= 0)-> int: # le damos un valor por default
    return a + b
resultado = sumar2()
print(f'resultado de la suma: {resultado}')
print(f'resultado de la suma: {sumar2(22,66)}')

# Argumentos, variables en funciones
def listarNombres(*nombres):
    for nombre in nmbres: # se va aconvertir en una tupla
        print(nombre)
listarNombres('lucas', 'jose', 'claudia', 'rosa', 'maria')
listarNombres('macos', 'daniel', 'romina', 'pepe', 'marcela')

def listarTerminos(**terminos): # lo mas utilizado es **kwargs para recibir los arguemtnos
    for llave, valor in terminos.items(): # kwargs significa: key word  argument
        print(f'{llave} : {valor}')

listarTerminos() # no recibe nada, nada se va a mostrar
listarTerminos(IDE='integrated develoment enviroment', PK='primaruy key')
listarTerminos(nombre='leonel messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['tito', 'pedro', 'carlos']
desplegarNombres(nombres2)
desplegarNombres('carla')
#desplegarNombres(10) # no es un objeto iterable
desplegarNombres((10, 11)) # la convertimos a una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22, 55 ]) # la convertimos en una lista

# funciones recursivas
def factorial(numero):
    if numero == 1: # caso base
         return 1
    else:
        return numero * factorial(numero-) # caso recursivo
numeroFactorial = int(input('digite el numero para calcular el factorial:'))
resultado = factorial(numeroFactorial) #codigo duro
print(f'el factorial del numero 5 es: {resultado} ') # tarea que el usuario ingrese el numero para calcular factorial
