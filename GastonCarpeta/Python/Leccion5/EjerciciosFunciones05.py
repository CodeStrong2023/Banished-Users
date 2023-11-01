#ejercicio 5: convertidor de temperatura
#realizar dos funciones para convertir de grados a celsius
# a fahrenheit y viseversa.
#investigar las formulas

# funcion que convierte de celsius a fahrenheir
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 # la presendecia: multiplicacion, division y suma

#funcion que convierte de fahrenheint a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # respetar la presendencia utilizando parentesis

celsius = float(input('digite el valor de clesius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

fahrenheit = float(input('digite el valor de fahrenheit:'))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> { resultado:2f}')