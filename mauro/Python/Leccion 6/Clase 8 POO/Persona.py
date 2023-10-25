# Creamos una clase
class Persona:
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostar_detalle(self): # Self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')


# Objeto 1
persona1 = Persona('Mauro', 'Mesas', 4405655, 21) # Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f'Nombre y Apellido: {persona1.nombre} {persona1.apellido} Edad: {persona1.edad}')

# Objeto 2
persona2 = Persona('Juan', 'Perez', 4545452, 21)
print(f'Nombre y Apellido: {persona2.nombre} {persona2.apellido} Edad: {persona2.edad}')


# Modificar los atributos de un objeto
persona1.nombre = 'Liliana'
persona1.apellido = 'Gomez'
persona1.edad = 24
print(f'(modificado) Nombre y Apellido: {persona1.nombre} {persona1.apellido} Edad: {persona1.edad}')


# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (acciones)

persona1.mostar_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostar_detalle()


# *Clase 9 (POO Parte 2)*

# Persona.mostar_detalle(persona1) # Debemos pasarle una referencia para el self o dará error.

# Crear Atributos Desde un Objeto
persona1.telefono = '44223355'
print(f'Este es el telefono: {persona1.telefono}')
# print(persona2.telefono) el objeto persona2 no tiene atributo, da error

# Método Init Dunder con Argumentos Variables
persona3 = Persona('Rogelio', 'Romero', 1123588, 22, 'Telefono', '1234561', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostar_detalle()

# Encapsulamiento
print(persona3._dni) # Esto no se debe utilizar en python, esto dice que lo desconocemos
# persona3.__nombre # Esta totalmente encapsulado (No acepta ningun tipo de cambio)
