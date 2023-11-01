# ejercicio 7: juego adivina el numero
#realizar un juego para adivinar un numero. para ello se debe
#generar un numero aleatorio entre 1 - 100 y luego ir pidiendo
#numeros indicando a N. el proceso termina cuando el usuario acierta
#y alli se debe mostrar el numero de intentos.
import random
aleatorio = random.randint(0,100) # toma de 0 a 100 literal, generamos un numero aleatorio
contador = 0
while True:
    numero = int(input("digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\tno es el numero, digite un numero menor")
    elif numero < aleatorio:
        print("\tno es el numero digite un numero mayor")
    else:
        print(f"felicidades, acabas de adivinar el numero {aleatorio}")
        break # rompe el ciclo y el blucle
        print(f"\n numeros de intentos: {contador}")