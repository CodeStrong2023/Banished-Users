'''ejercicio1: determinar si un alumno apueba o reprueba un curso, sabiendo que aprobara si su pronedio de tres calificaciones es mayot o igual a 70 reprueba caso contrario.
def determinar_aprobacion(calificacion1, calificacion2, calificacion3):
    promedio = (calificacion1 + calificacion2 + calificacion3) / 3
    if promedio >= 70:
        return "Aprobado"
    else:
        return "Reprobado"

# Ejemplo de uso
calif1 = float(input("Ingrese la primera calificación: "))
calif2 = float(input("Ingrese la segunda calificación: "))
calif3 = float(input("Ingrese la tercera calificación: "))

resultado = determinar_aprobacion(calif1, calif2, calif3)
print("El alumno está", resultado)
'''
'''
ejercicio2: en un almacen se hace un 20 de descuento a 
los clientes cuyacompra supere los $100. ?cual sera la 
cantidad que pagara una persona por su compra?

def calcular_total_compra(monto_compra):
    if monto_compra > 100:
        descuento = monto_compra * 0.2
        total_pagar = monto_compra - descuento
    else:
        total_pagar = monto_compra
    return total_pagar

# Ejemplo de uso
monto = float(input("Ingrese el monto de compra: "))

total = calcular_total_compra(monto)
print("El total a pagar es:", total)
'''
ejercicio4: leer 2 numeros: si son iguales que los


