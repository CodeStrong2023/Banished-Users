""" esta clase veremos la sentencia if/else# f condicion == True
    print('condicional verdadera')
elif condicional == False:
    print('condicional falsa')
else:
    print('condicional sin especificar')
"""
''' = int(input('digite un numero en el rango de 1 al 3'))
numTexto = ''
if num == 1:
    numTexto = 'numero uno'
elif num == 2:
    numTexto = 'numero dos'
elif num == 3:
    numTexto = 'numero tres'
else:
    numTexto ='has ingresado un numero fuera de rango'
print(f'el numero ingresado es : {num} - {numTexto}')''''''
condicion = False
if condicion:
    print('condicion verdadera')
else:
print('condicion falsa')

print('condicion verdadera') if condicional else print ('condicion falsa')

'''
'''
# imprimir numeros del 0 al 5 con el ciclo while
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador +=1
'''
'''
#ciclo for
cadena = 'hello' 
for letra in cadena:
    print(letra)
else:
    print('fin del ciclo for')
''''''palabra reservada break
for letra in 'alemania':
    if letra == 'a':
        print(f'letra encontrada: {letra}')
        break
else:
    print('fin del ciclo for')
''''''
#palabra reservada continue
for i in rango(6):
    if i % 2 == 0:
        print(f'valor: {i}')
for i in range(6):
    if i % 2 !=0:
        continue
    print(f'valor: {i}')
'''
