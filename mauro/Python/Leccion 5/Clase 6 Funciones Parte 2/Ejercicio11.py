# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. 
# Crear un diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendrá el siguiente menú de opciones
# 1. Nuevo contacto
# 2. Borrar contacto
# 3. Ver contactos existentës
# 4. Salir

agenda = {}
while True:
    print('\n\t .: MENÚ :.')
    print('1. Nuevo Contacto')
    print('2. Borrar Contacto')
    print('3. Ver Contactos Existentes')
    print('4. Salir')
    opcion = int(input('Digite una opción: '))
    print()

    if opcion == 1:
        nombre = input('Digite el nombre del contacto: ')
        telefono = input('Digite el numero del telefono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente!')
        else:
            print('Este nombre de contacto ya existe')
    elif opcion == 2:
        nombre = input('Cual es el nombre del contacto?: ')
        if nombre in agenda:
            del(agenda[nombre])
            print('Se ha eliminado el contacto')
        else:
            print('El conctacto ingresado no existe en la agenda')
    elif opcion == 3:
        print('Agenda de contactos')
        for clave, valor in agenda.items(): #Funcion para mostrar clave y valor
            print(f'Nombre: {clave}, Telefono: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos')
        break
    else:
        print('Se equivoco de opción de menú')
    print()