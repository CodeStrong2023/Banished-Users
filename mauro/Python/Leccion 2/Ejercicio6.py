#Ejercicio 6: Etapas de vida según la edad

edad = int(input("Digite su edad: "))
mensaje = None
if 0 <= edad < 10:
    mensaje = "La infancia es increible y bella"
elif 10 <= edad < 19:
    mensaje = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo"
else:
    mensaje = "Etapa de vida no reconocida"
print(f"Tu edad es: {edad}, {mensaje} ")