# En esta clase veremos sentencia if/else
"""
condicion = "Hola"
if condicion == True:
    print("Condición Verdadera")
elif condicion == False:
    print("Condición Falsa")
else: 
    print("Condición sin Especificar")
"""
"""
#Ejercicio número a texto
num = int(input("Digite un número en el rango del 1 al 3: "))
numTexto = ''
if num == 1:
    numTexto = "Número uno"
elif num == 2:
    numTexto = "Número dos"
elif num == 3:
    numTexto = "Número tres"
else:
    numTexto = "Has ingresado un número fuera de rango"
print(f"El número ingresado es: {num} - {numTexto}")
"""

#Operador Ternario
condicion = True
#if condicion: 
#    print("Condición Verdadera")
#else:
#    print("Condición Falsa")

condicion("Condición Verdadera") if condicion else print ("Condición Falsa")