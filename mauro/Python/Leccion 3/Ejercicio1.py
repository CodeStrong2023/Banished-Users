#Ejercicio 1: Año Bisiesto
while True:
    año = int(input("Ingrese el año que desea saber si es bisiesto: "))
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")

    respuesta = input("¿Desea saber otro año? (si/no): ")
    if respuesta != "si":
        break