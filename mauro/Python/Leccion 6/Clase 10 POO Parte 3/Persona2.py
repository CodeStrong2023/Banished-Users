class Persona2:
    def __init__(self, nombre, apellido, edad): # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos modificados a mostar son los siguientes: {self._nombre} {self._apellido} edad: {self._edad}')

# GETTER
    @property # Decorador
    def nombre(self): # Método Getter
        print("Estamos utilizando el método get")
        return self._nombre
    
# SETTER    
    @nombre.setter
    def nombre(self, nombre): # Método Setter
        print("Estamos utilizando el método set")
        self._nombre = nombre

# Tarea: Get y Set de apellido y edad
# Apellido
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

# Edad
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self): # Método Destructor
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')
    
if __name__ == '__main__':
    persona1 = Persona2("Mauro", "Mesas", 21)
    print(persona1.nombre) # Llamamos al método getter
    persona1.nombre = 'Juan Pedro' # Llamamos el método setter
    print(persona1.nombre) # Método getter
    print(persona1.mostrar_detalles()) # Método mostar detalles
# Atributo read-only seria la edad porque no tiene el método set
    print(persona1.edad)

# TAREA: crear tres objetos más, utilizando los métodos getter and setter
# para modificar, y mostrar los cambios con método "mostrar detalles"
#1
    persona2 = Persona2("Carlos", "Tevez", 39)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = "Carlitos"
    persona2.apellido = "Gomez"
    persona2.edad = 40
    print(persona2.mostrar_detalles())
#2
    persona3 = Persona2("Juliana", "Sanchez", 30)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = "Juli"
    persona3.apellido = "Gonzalez"
    persona3.edad = 32
    print(persona3.mostrar_detalles())
#3
    persona4 = Persona2("Juan", "Hernandez", 21)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = "Juancito"
    persona4.apellido = "Moreno"
    persona4.edad = 25
    print(persona4.mostrar_detalles())

    print(__name__) # Para que no se vea en PruebaPersona2 (if + __name__..)

