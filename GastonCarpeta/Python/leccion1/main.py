'''
miVariable = 3
print(miVariable)
miVariable = "hola a todos los alumnos de la tecnicatura "
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(z)
print(id(x))


# Tipos int, float, String, bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
X = True
print(x)
print(type(x))
x = False
print(type(x))

# manejos de cadenas (String)
miGrupoFavorito = "red hot chilli peppers:"
caracteristicas = "the best rock band"
print("mi grupo faborito es: ", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# tipos boleanos (bool)
miBoleano = 3 > 2
print(miBoleano)

if miBoleano:
    print("el resultado es verdadero")
else:
    print("el resultado es falso")

# procesar la entrada del ususario
# funcion input
# resultado = input("digite un numero: ")  # regrese un dato tipo String
# print(resultado)

# conversion de la entrada de datos
numero1 = int(input("escribre el primer numero: "))
numero2 = int(input("escribe el segundo numero: "))
resultado = numero1 + numero2
print(" el resultado de la suma es: ", resultado)
'''
"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print("resultado de la suma: ", suma)
print(f'el resultado de la suma es: {suma}')

resta = operandoA - operandoB
print(f"el resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"el resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"el resultado de la division es : {division}")
division =operandoA // operandoB
print(f"el resultado de la division (int) es: {division}")
modulo = operandoA % operandoB
print(f"el resultado de la division o residuo (mudulos) es: {modulo}")
exponente = operandoA ** operandoB
print(f"el resultado del exponente es: {exponente}")
"""
"""
alto = int(input('proporciona el alto del rectangulo: '))
ancho = int(input('proporciona el ancho del rectangulo'))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('area: ',area)
print('perimetro: ', perimetro)
"""
"""
miVariable3 = 10
print(miVariable3)

# operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 *3
miVariable3 *= 3
print(miVariable3)

# # miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

# operadores de comparacion

d = 4
b = 6
resultado = d == b  # comprobamos si son iguales
print(resultado)

# operador diferente
resultado = d != b
print(resultado)

# operador mayor que
resultado = d > b
print(resultado)

# operador menor que
resultado = d > b
print(resultado)

# operador menor o igual que
resultado = d <= b
print(resultado)

# operador mayor o igual que
resultado = d >= b
print(resultado)
"""

"""
a = int(input("digite un numero: "))
print(f"el residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"el valor de a es: {a} es un numero PAR")
else:
    print(f"el valor de a es: {a} es un numero IMPAR")
"""
"""
edadAdulto = 18
edadPersonas = int(input("digite su edad: "))

if edadPersonas >= edadAdulto:
    print(f"su edad es: {edadPersona} años, usted es mayorr de edad")
else:
    print(f"su edad es: {edadpersona} años, usted es menor de edad")
"""
"""
# operadores logicos

a = True
b = True
resultado = a and b
print(resultado)

# operador or
resultado = a or b
print(resultado)

# operador not
resultado = not a
print(resultado)
"""
"""
# ejercicio: valor dentro de un rango
valor = int(input("digite un numero dentro del rango 0 al 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f'el valor {valor} esta dentro del rango')
else:
    print(f' el valor {valor} no esta dentro del rango')
"""
"""
# ejercicio con el operador or, operador not
vacaciones = False
diaDescanso =False
if not (vacaciones or diaDescanso):
    print('tiene trabajo que hacer')
else:
    print('puede asistir al juego')
"""
"""
# ejercicio: rango entre 20 y 30 años
edad = int(input("digite su edad: "))
# veinte = edad >= 20 and edad < 30
# print(veinte)
# treinta = edad >= 30 and edad < 40
# print(treinta)

#if veinte or treinta:
if (20<= edad < 30) or (30 <= edad < 40):  # sintaxis simplificada del operador and
    print("estas dentro del rango del rango de los (20'0) a (30'0) años")
#    if veinte:
#       print('estas dentro del rango de los (20\'0) años')
#elif treinta:
#       print('estas dentro del rango de los (30\'0)')
#else:
    #print('no estas dentro del rango del rango ')
"""
"""
numero1 = int(input('digite el valor para el numero1: '))
numero2 = int(input('digite el valor para el numero 2: '))

# ejercicio: el mayor de dos numeros
if numero1 > numero2:
    print('el numero 1 es mayor')
else:
    print('el numero 2 es mayor')
"""
"""
# ejercicio: tienda de libros
print('digite los siguientes datos del libro')
nombre = input('digite el nombre del libro: ')
id = int(input('digite el ID del libro:'))
precio = float(input('digite el precio del libro:'))
envioGratuito = input('indicar si el libro es gratuito (true/false): ')
if envioGratuito == True:
    envioGratuito = True
elif envioGratuito == False:
    envioGratuito = False
else:
    envioGratuito = 'el valor es incorrecto, debe escribir True/False'
print(f'''
        Nombre: {precio}
        Id: {id}
        Precio:{precio}
        Envio gratuito?: {envioGratuito}
'''
