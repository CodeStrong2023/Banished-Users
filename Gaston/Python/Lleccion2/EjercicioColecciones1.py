#ejercicio 1: eliminar duplicados de una lista
#escriba un programa donde tenga una lista y que a continuacion
#elimine los lementos repetidos, por ultimo mostrar la lista.

#creamos una lista
lista = [1,2,3,"Ariel",7,7,3,"Alberto",1,"Ariel",2,"Alberto"]
conjunto = set(lista) # convertimos la lista a un conjunto de tipo set
#lista =  list(conjunto) #convertimos el conjunto en una lista
lista = list(set(lista)) # la conversion hecha en una sola linea de codigo (mas eficiente)
print(lista)




