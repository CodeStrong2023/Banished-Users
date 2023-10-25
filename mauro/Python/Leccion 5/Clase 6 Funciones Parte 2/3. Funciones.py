# Paso de argumentos (Funciones)

def mi_funcion2(name, lastName):
    print('Hola!')
    print(f'Nombre: {name}, Apellido: {lastName}')

mi_funcion2('Juan', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Maria', 'Gonzalez')


# Return en Funciones
# Creamos una función para sumar
def sumar(a,b):
    return a + b

# resultado = sumar(78,22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 34)}')


def sumar2(a = 0 , b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22,66)}')

# Argumentos, variables en funciones
def listarNombres(*nombres): # Normalmente se utiliza: *args
    for nombre in nombres:  # Se va a convertir en una tupla
        print(nombre)

listarNombres('Lucas', 'Jose', 'Rosa', 'Maria')
listarNombres('Marcos', 'Daniel', 'Romina', 'Carlos')