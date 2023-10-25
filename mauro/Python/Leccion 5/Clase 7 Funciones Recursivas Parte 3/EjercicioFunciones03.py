# Ejercicio 3: Función Recursiva
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el número 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan números negativos no imprime nada

def imprimirNumRecursivos(numero):
    if numero >= 1: # Caso Base
        print(numero)
        imprimirNumRecursivos(numero-1) # Caso Recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto...')

numeroF = int(input('Digite un número: ')) # Tarea
imprimirNumRecursivos(numeroF)
