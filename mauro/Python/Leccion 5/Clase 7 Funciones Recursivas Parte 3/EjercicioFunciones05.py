# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius a fahrenheit y viseversa.
# Investigar las formulas

# Función Para Convertir Celsius a Fahrenheit
def celsiusFar(celsius):
    return celsius * 9 / 5 + 32

# Función Para Convertir Fahrenheit a Celsius
def fahrenheitCel(fahren):
    return (fahren - 32) * 5 / 9

# Comprobación
celsius = float(input('Digite el valor de celsius: '))
resultado = celsiusFar(celsius)
print(f'{celsius}° Celsius a Fahrenheit: {resultado:.2f}')

fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado = fahrenheitCel(fahrenheit)
print(f'{fahrenheit}° Fahrenheit a Celsius: {resultado:.2f}')