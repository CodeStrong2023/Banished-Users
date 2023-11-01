'''
ejercicio 1:
deberemos plasmar la expresion en una expresion,
 algoritmica' osea hacerla en codigo'''
'''
a = float(input('digite el valor de a: '))
b = float(input('digite el valor de b: '))
c = float(input('digite el valor de c: '))
resultado = (a ** 3*(b ** 2 - 2 * a *c))/(2 * b)
print(f'el resultado es: {resultado}')

'''


'''

#ejercicio año bisisesto
def es_bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Ciclo principal
while True:
    año = int(input("Ingrese un año (0 para salir): "))
    if año == 0:
        break
    if es_bisiesto(año):
        print(f"El año {año} es un año bisiesto.")
    else:
        print(f"El año {año} no es un año bisiesto.")'''

'''
#ejercicio calcular la suma de n
def calcular_suma(n):# ejercicio calcular la suma de n
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

# Ejemplo de uso
n = int(input("Ingrese el valor de N: "))

resultado = calcular_suma(n)
print("La suma de los", n, "primeros números es:", resultado)
'''
'''
def contar_numeros(numeros):
    positivos = 0
    negativos = 0
    neutros = 0

    for numero in numeros:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            neutros += 1

    return positivos, negativos, neutros

# Leer 10 números
numeros = []
for i in range(10):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Contar positivos, negativos y neutros
pos, neg, neu = contar_numeros(numeros)

# Mostrar resultados
print("Cantidad de números positivos:", pos)
print("Cantidad de números negativos:", neg)
print("Cantidad de números neutros:", neu)
''''''

def calcular_promedio(calificaciones):
    total = sum(calificaciones)
    promedio = total / len(calificaciones)
    return promedio

def encontrar_calificacion_mas_baja(calificaciones):
    calificacion_mas_baja = min(calificaciones)
    return calificacion_mas_baja

# Leer las calificaciones de los alumnos
calificaciones = []
for i in range(10):
    calificacion = float(input(f"Ingrese la calificación del alumno {i+1}: "))
    calificaciones.append(calificacion)

# Calcular promedio
promedio = calcular_promedio(calificaciones)

# Encontrar calificación más baja
calificacion_baja = encontrar_calificacion_mas_baja(calificaciones)

# Mostrar resultados
print("La calificación promedio del grupo es:", promedio)
print("La calificación más baja del grupo es:", calificacion_baja)
'''
'''

def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Pedir al usuario que ingrese un número
numero = int(input("Ingrese un número entero mayor o igual a 0: "))

# Verificar si el número es válido
if numero < 0:
    print("Error: El número debe ser mayor o igual a 0.")
else:
    # Calcular el factorial
    resultado = calcular_factorial(numero)
    print("El factorial de", numero, "es:", resultado)
''''''
def calcular_suma_pares(numeros):
    suma_pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            suma_pares += numero
    return suma_pares

def contar_numeros_pares(numeros):
    contador_pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            contador_pares += 1
    return contador_pares

def calcular_promedio_impares(numeros):
    impares = [numero for numero in numeros if numero % 2 != 0]
    if len(impares) > 0:
        promedio = sum(impares) / len(impares)
    else:
        promedio = 0
    return promedio

# Leer la lista de números enteros
numeros = []
n = int(input("Ingrese la cantidad de números a ingresar: "))
for i in range(n):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Calcular suma de números pares
suma_pares = calcular_suma_pares(numeros)

# Contar números pares
contador_pares = contar_numeros_pares(numeros)

# Calcular promedio de números impares
promedio_impares = calcular_promedio_impares(numeros)

# Mostrar resultados
print("La suma de los números pares es:", suma_pares)
print("La cantidad de números pares es:", contador_pares)
print("El promedio de los números impares es:", promedio_impares)
'''
def calcular_salario(horas_trabajadas, tarifa):
    salario = horas_trabajadas * tarifa
    return salario

# Variables para almacenar la sumatoria de los salarios
sumatoria_salarios = 0

# Ciclo para ingresar los datos de las 5 personas
for i in range(5):
    horas_trabajadas = float(input(f"Ingrese las horas trabajadas de la persona {i+1}: "))
    tarifa = float(input(f"Ingrese la tarifa de pago de la persona {i+1}: "))

    # Calcular salario de la persona
    salario = calcular_salario(horas_trabajadas, tarifa)
    sumatoria_salarios += salario

    print(f"El salario de la persona {i+1} es: {salario}")

print("La sumatoria de todos los salarios es:", sumatoria_salarios)
