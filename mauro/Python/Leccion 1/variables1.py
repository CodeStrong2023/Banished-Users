'''
miVariable = 3
print(miVariable)
miVariable = "a"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
#Las literales se guardan u escriben en (x + ultimos 3 nums, ej: x257)
print(id(y))
print(id(z))

#Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x)) 

#Manejo de cadenas (String)
miGrupoFavorito = "The Letter Black: "
caracteristicas = "The best rock band"
print("Mi grupo favorito es: "+miGrupoFavorito) #Concatenacion con simbolo "+"
print("Mi grupo favorito:", miGrupoFavorito, caracteristicas) #Concatenacion con simbolo ","

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2)) #Convertir str a int para sumar variables str

#Tipos Boleanos (bool)
miBooleano = 5 < 2
print(miBooleano)

if miBooleano:
	print("El resultado es Verdadero")
else:
	print("El resultado es Falso")

#Procesar la entrada del ususario
#Funcion input
resultado = input("Digite un numero: ") #input regresa un dato tipo string
print(resultado)

#Conversión de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
'''
"""
#Operadores Aritmeticos e Interpolacion
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("Resultado de la suma:", suma) #Concatencacion con ,
print(f'El resultado de la suma es: {suma}') #Interpolacion

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")

division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")

modulo = operandoA % operandoB
print(f"El resultado de la division o residuo (modulo) es: {modulo}")

exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")
"""
"""
#Ejercico del Rectangulo
alto = int(input('Proporciona el alto del rectangulo: '))
ancho = int(input('Proporciona el ancho del rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('Área: ',area)
print('Perimetro: ',perimetro)
"""
"""
miVariable3 = 10
print(miVariable3)

#Operadores de Reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

#miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

#miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

#miVariable3 = miVariable3 / 2
miVariable3 //= 2
print(miVariable3)

#Operadores de Comparación

d = 4
b = 2
resultado = d == b #Operador igual
print(resultado)

resultado = d != b # Operador diferente
print(resultado)

resultado = d > b # Operador mayor que
print(resultado)

resultado = d < b # Operador menor que
print(resultado)

resultado = d <= b # Operador menor o igual que
print(resultado)

resultado = d >= b # Operador mayor o igual que
print(resultado)
"""
"""
#Ejercicio: número par o impar
a = int(input("Digite un número: "))
print(f"El resultado de la division es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es: {a} es un número PAR")
else:
    print(f"El valor de a es: {a} es un número IMPAR")
"""
"""
#Ejercicio: determinar si es mayor de edad
edadAdulto = 18
edadPersona = int(input("Digite su edad: "))
if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, usted es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años, usted es menor de edad")
"""
"""
#Operadores Lógicos

a = True
b = False
#AND
resultado = a and b #Devuelve True si ambos operadores son True
print(resultado)
#OR
resultado = a or b #Devuelve True si alguno de los operandos es True
print(resultado)
#NOT
resultado = not a #Devuelve True si alguno de los operandos es False (cambia valor)
print(resultado)
"""
"""
#Ejercicio: Valor dentro de un rango
valor = int(input("Digite un número: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} No esta dentro del rango")
"""
"""
#Ejercicio con el operador or, operador not
vacaciones = False
diaDescanso = True
if not (vacaciones or diaDescanso):
    print("Puede asistir al juego")
else:
    print("Tiene trabajo que hacer")
"""
"""
#Ejercicio: Rango entre 20 y 30 años
edad = int(input("Digite su edad: "))
#veinte = edad >= 20 and edad < 30
#print(veinte)
#treinta = edad >= 30 and edad < 40
#print(treinta)

#if veinte or treinta:
if (20 <= edad < 30) or (30 <= edad < 40): #Sintaxis simplificada del operador and
    print('Estas dentro del rango de los (20\'0) a (30\'0) años)')
#    if veinte:      #Las tabulaciones en python se llamas identacion
#        print("Estas dentro del rango de los (20'0) años)")
#    elif treinta:
#        print("Estas dentro del rango de los (30'0) años)")
else:
    print('No estas dentro del rango de los (20\'0) a (30\'0) años)') #comillas simples '' y backslash \
"""
"""
#Ejercicio: El mayor de dos números
numero1 = int(input("Digite el valor para el número 1: "))
numero2 = int(input("Digite el valor para el número 2: "))

if numero1 > numero2:
    print("El número 1 es mayor")
else:
    print("El número 2 es mayor")
"""

#Ejercicio: Tienda de Libros
print("Digite los siguientes datos del libro: ")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el ID del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar si el libro es gratuito (True/False): ")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto, debe escribir True/False"
print(f"""
        Nombre: {nombre}
        Id:{id}     
        Precio:{precio}
        Envio Gratuito?: {envioGratuito}
""")
