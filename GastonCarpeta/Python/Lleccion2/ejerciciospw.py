'''#ejercicio calcular la estacion del año

mes = int(input('digite un mes del año (1 - 12): '))
estacio = None
if mes == 1 or mes == 2 or mes == 3:
    estacion = 'verano'
elif mes == 4 or mes == 5 or mes == 6:
    estacion ='otoño'
elif mes == 7 or mes == 8 or mes == 9:
    estacion = 'invierno'
elif mes == 10 or mes == 11 or mes == 12:
    estacion = 'primavera'
else:
    estacion = 'error, no hay numero para ese mes'
print(f'para el mes {mes} la estacion es: {estacion}')
'''




#ejercicio: sistema de calidicaciones

'''
calificaciones = int(input('digite una calificacion entre o y 10:'))
if 9 <= calificacion <= 10:
    print('A')
elif 8 <= calificacion < 9:
    print('b')
elif 7 <= calificacion < 8:
    print('c')
elif 6 <= calificacion < 7:
    print('d')
elif 0 <= calificacion < 6:
    print('f')
else:
    print('valor incorrecto...')
'''

#ejercicio: sistema de calificaciones
calificacion = int(input('digite una calificacion entre o y 10:'))
if 9 <= calificacion <= 10:
    print('a')
elif 8 <= calificacion < 9:
    print('b')
elif 7 <= calificacion <8:
    print('c')
elif 6 <= calificacion < 7:
    print('d')
elif 0 <= calificacion < 6:
    print('f')
else:
    print('valor incorrecto...')
'''
#ejercicio etapas de vida segun la edad
edad = int(input('digite su edad: '))
mensaje = None
if 0 <= edad < 10: #sintaxis simplificada
    mensaje = 'tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 20:
    mensaje = 'tienes muchos cambios, mucho que estudiar'
elif 20 <= edad <30:
    mensaje = 'amor y comienza el trabajo'
    #debemos agregar para las demas edades
else:
    mensaje = 'error, etapas de vida no reconocida'
print(f'tu edad es: {edad}, {mensaje} ')'''
