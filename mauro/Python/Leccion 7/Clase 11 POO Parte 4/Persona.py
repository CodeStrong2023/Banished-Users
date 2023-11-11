# Clase 11: Herencia
class Persona:
    def __init__(self, nombre ,edad):
        self.nombre = nombre
        self.edad = edad
    @property
    def nombre(self):
        return self.nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre
    
    @property
    def edad(self):
        return self.edad
    
    @edad.setter
    def edad(self, edad):
        self.edad = edad
    
    def __str__(self): #Override = sobreescribir
        return f"Persona: {self._nombre} {self._edad}"
        

class Empleado(Persona): # Esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    @property
    
    def sueldo(self):
        return self.sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self.sueldo = sueldo
    
    def __str__(self):
        return f"Empleado: [ Sueldo: {self.sueldo}] {super().__str__()}"

empleado1 = Empleado("Mauro", 21 ,80000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)  

# Tarea: Encapsular los atributos y agregar los metodos getters and setters
# Crear otro objeto, pasar los datos para nombre ,edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente.

empleado2 = Empleado("Maria" , 28, 75000)
print(empleado2.nombre)
print(empleado2.edad)
empleado2.nombre = "Juana"
empleado2.edad = 21
empleado2.sueldo = 20000

print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)



    

    


  