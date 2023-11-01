#ejercicio 2: modificar los elementos de una lista
# llenar una lista con los numeros del 1 al 10, luego modificar los
#elementos de la lista multiplicados por un valor ingresado por le usuario
lista = list(range(1,11))
print('lista Original')
for i in lista:
    print(i, end='-')
valor = int(input('\nDigite un valor a multiplicar: '))
# multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista):#funcion para modofocar los indices de la lista
    lista[indice] *= valor # el iterador solo recorre los indices, en esta linea se multiplica

print(f'lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i, end=)


