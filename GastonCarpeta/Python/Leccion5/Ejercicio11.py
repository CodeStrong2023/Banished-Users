#ejercicio 11: agenda telefonica
#hacer un programa que simule una agenda de contactos. crear un diccionario
#donde la clave sea el nombre del usuario y el valor
#sea el telefono, programa tendra el siguiente menu de opciones:
#1.nuevo contacto
#2. borrar contacto
#3. ver contactoss existentes
#4. salir
agenda ={}
while True:
    print('\t.:MENU:. ')
    print('1. nuevo contacto')
    print('2. borrar cpntacto')
    print('3. ver contacto')
    print('4.salir')
    opcion = int(input('digite el nombre del contacto:'))
    if opcion == 1:
        nombre = input('digite el nombre del contacto:')
        telefono = input('digite el numero de telefono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('contcto agregado exitosamente!')
        else:
            print('este nombre de contacto ya existe')
    elif opcion == 2:
        nombre = input('cua es el nombre del contacto: ')

if nombre in agenda:
    del (agenda[nombre])
    print('se ha eliminado el contacto requerido')
    else:
        print('este contacto no existe en la agenda')
    elif opcion == 3:
        print('agenda de contactos')
        for clave, valor in agenda.items():
            print(f'nombre: {clave},telefono: {valor}')
    elif opcion == 4:
        print('gracais por utilizar su agenda de contactos')
        break
    else:
        print('se equivoco de opcion de menu')
    print()



