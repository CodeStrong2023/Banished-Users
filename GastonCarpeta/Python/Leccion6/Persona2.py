class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')


    @property # decorator
    def nombre(self): # metodo getter
        print('estamos utilizando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): #metodo setter
        print('estamos utilizando el metodo set')
        self._nombre = nombre
    @property.setter
    def apellido(self):
        return self._apellido

    @property.setter
    def apellido(self,apellido):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    #@edad.setter
    #def edad(self, edad):
     #   self._edad = edad

    def __del__(self):
        print(f'persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('ariel', 'betancud', 41)
    print(persona1.nombre) #llamamos al metodo getter
    persona1.nombre = 'juan pedro'#llamamos el metodo setter
    print(persona1.nombre)#otra vez con el metodo getter
    print(persona1.mostrar_detalles())# llamamos el metodo mostrar detalles
    #atributo read-only (solo lectura) seria la edad porque no tiene el metodo set
    print(persona1.edad)
    # tarea crear tres objetos mas utilizando los metodos getter and setter
    # para modificar, y mostrar los cambios
    #objeto numero 1 de la tarea
    persona2 = Persona2('flor', 'romero', 23)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalles())
    persona2.nombre = 'florencia'
    persona2.apellido = 'romer'
    persona2.edad = 22


    #objeto numero dos de la tarea
    persona3 = Persona2('caro', 'felisa', 21)
    persona3.nombre = 'carolina'
    persona3.apellido = 'felix'
    persona3.edad = 31
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalles())

    # objeto numero tres de la tarea
    persona4 = Persona2('naty', 'luccer', 35)
    persona4.nombre = 'natalia'
    persona4.apellido = 'lucero'
    persona4.edad = 33
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona4.mostrar_detalles())

    print(__name__)