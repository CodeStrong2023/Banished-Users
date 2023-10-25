# Argumentos Variables para Diccioario

def listTerminos(**kwargs): # La mas utilizada es kwargs
    for llave, valor in kwargs.items(): # Kwargs = Key Word Arguments
        print(f'{llave} : {valor}')

# Comprobación
listTerminos() # No recibe nada, nada se va a mostrar
listTerminos(IDE = 'Integrated Develoment Enviroment', PK = 'Primary Key')


# Lista de elementos con funciones (convertir)
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10, 11) # No es un objeto iterable
desplegarNombres((10, 11)) # La convertimos a una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22, 55]) # La convertimos en una lista


# Funciones Recursivas
def factorial(numero):
    if numero == 1: # Caso Base
        return 1
    else:
        return numero * factorial(numero-1)
    
#resultado = factorial(5) # Código Duro
#print(f'El factorial del número 5 es: {resultado}')

# Comprobación con datos ingresados
numeroFact = int(input('Digite el num para calcular el factorial: '))
resultado = factorial(numeroFact)
print(f'El Factorial del número {numeroFact} es: {resultado}')