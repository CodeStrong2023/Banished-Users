#ejercicio 2: funciones con *args para multiplicar
#crear una funcion para multiplicar los valores recibidos
# de tipo numerico, utilizando argumentos variables *args
#como parametros de la funcion y regresar como resultado
#la multiplicacion de todos los valores pasados como arguementos

# definimos la funcion para multiplicar
def multiplicar_valores(*numeros):
    resultado = 1 # el cero no nos ayuda a multiplicar
    for numero in numeros:
        resultado *= numero
    return resultado


# llamamos la funcion
print(multiplicar_valores(3,5,15)) # le pasamos los arguementos