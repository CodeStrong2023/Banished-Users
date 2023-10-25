diccionarioNuevo = {"azul": "blue", "rojo": "red", "verde": "green", "amarillo": "yellow"}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo["azul"])
print(diccionarioNuevo)

# Los diccionarios pueden alamacenar diferentes tipos de datos
diccionario2 = {"Juan": {"edad": 21, "altura": 1.80}, "Rodrigo": [30, 1.85], "Camila": [35, 1.77]}
print(diccionario2)


seleccionArgentina = { 
    10 : { "Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio":"50 Millones", "Posicion": "Extremo derecho"},
    11 : { "Nombre": "Ángel Di María", "Edad": 34, "Altura": 1.80, "Precio":"12 Millones", "Posicion": "Extremo derecho"},
    21 : { "Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio":"35 Millones", "Posicion": "Media punta"},
    19 : { "Nombre": "Nicolás Otamendi", "Edad": 34, "Altura": 1.83, "Precio":"3.5 Millones", "Posicion": "Defensa Central"},
    1  : { "Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio":"3.5 Millones", "Posicion": "Portero"},
    # Tarea: agregar jugadores
    17 : { "Nombre": "Papu Gomez", "Edad": 35, "Altura": 1.67, "Precio":"2 Millones", "Posicion": "Extremo izquierdo"},
    23 : { "Nombre": "Dibu Martínez", "Edad": 31, "Altura": 1.95, "Precio":"28 Millones", "Posicion": "Portero"},
    3  : { "Nombre": "Nicolás Tagliafico", "Edad": 31, "Altura": 1.72, "Precio":"9 Millones", "Posicion": "Lateral izquierdo"},
    7  : { "Nombre": "Rodrigo de Paul", "Edad": 29, "Altura": 1.80, "Precio":"40 Millones", "Posicion": "Mediocentro"},
    }

for llave, valor in seleccionArgentina.items(): # Se usa la funcion items para cargar todo lo del diccionario, en vez de la funcion value
    print(llave, valor)

print("La cantidad de jugadores cargados es de: ",end= "")
print(len(seleccionArgentina))

# Otra forma de recorrer el diccionario (Visto en clase 4)
#for i in seleccionArgentina:
#    print(f"{i} -> {seleccionArgentina[i]}")

