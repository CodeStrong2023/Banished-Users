# Ejercicio 2: Función con *args para multiplicar
# Crear una función para multiplicar los valores recibidos de tipo numérico,
# utilizando argumentos variables *args como parámetro de la función y regresar
# como resultado la multiplicación de todos los valores pasados como argumento

# Definimos función
def multi(*args):
    resultado = 1 # Se coloca 1, por que x 0 no ayuda a multiplicar
    for numero in args:
        resultado *= numero
    return resultado

# Llamamos a la función
print(multi(5,6,7)) # Le pasamos argumentos  