#ejercicio 5: factorial de un numero positivo
#hacer un programa para calcular el factorial de un numero positivo
numero = int(input("digite un numero"))
while numero < o: # mientras el numero sea negativo
    print("error -> el numero tiene que ser positivo ")
    numero = int(input("digite un numero: "))
    factorial = 0 # la variable para calcular el factorial
    for i in range(1,numero+1):
        factorial *= i
print(f"\n el factorial del numero { numero}positivo ingresado es: {factorial}")