# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe generar un número aleatorio entre 1 - 100
# Luego ir pidiendo números indicando 'es mayor' o 'es menor' según sea mayor o menor con respecto a N 
# El proceso termina cuando el usuario acierta y allí se debe mostrar el número de intentos

import random

print('\t.:Juego adivina el número:.')
aleatorio = random.randint(0,100) # Genera un num aleatorio de 0 a 100
contador = 0

while True:
    número = int(input('Digite un número: '))
    contador += 1
    if número > aleatorio:
        print('\t No es el número, digite un número MENOR')
    elif número < aleatorio:
        print('\t No es el número, digite un número MAYOR')
    else:
        print(f'Felicidades encontraste el número {aleatorio}')
        break # Se rompe el ciclo si se encontró el número

print(f'\n Numero de intentos: {contador}')