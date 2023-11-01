# en esta clase veremos la sentencia if/else
"""condicion = True
if condicion == True:
    print("condicion verdadera")
elif condicion == False:
    print("condicion falsa")
else:
    print('condiciones sin especificar')
"""

num = int(input('digite un numero en el rango del 1 al 3: '))
numTexto = ''
if num == 1:
    numTexto = 'numero uno'
elif num == 2:
    numTexto = 'numero uno'
elif num == 3:
    numTexto = 'numero tres'
else:
    numTexto = 'ha ingresado un numero fuera de rango'
print(f'el numero ingresado es: {num} - {numTexto}')