# ejercicio 01: crear una funcion para sumar los valores recibidos de tipo
#numerico, utilizando argumentos variables *args como parametros de la
# funcion y agregar como resultado la suma de todos los valores pasados
# como argumentos.
# definimos una funcion
def sumar_valor(*args): # recicimos una cantidad de parametros indefinidos
   resultado = 0
   # iteramos cada elemento
   for valor in args:
      resultado += valor
   return resultado

# llamamos a la funcion
print(sumar_valor(3,5,9))