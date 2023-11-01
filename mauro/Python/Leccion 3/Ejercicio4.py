#Ejercicio 4: Calificaciones de 10 alumnos
suma = 0
calificacion_baja = 99999

for i in range(1, 11):
    calificacion = float(input(f"{i} Digite una calificacion: "))
    suma += calificacion
    
    if calificacion < calificacion_baja:
        calificacion_baja = calificacion
        
calificacion_promedio = suma/10

print("La calificacion promedio es:", calificacion_promedio)
print("La calificacion baja es:", calificacion_baja)