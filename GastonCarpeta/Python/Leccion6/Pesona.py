class Persona:#creamos una clase

    def __init__(self, nombre, apellido, edad, *args, **kwargs):# se lo llama metodo init dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # este atributo esta capsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.wkargs = kwargs
    def mostrar_detalle(self):# self es igual a this
        print(f'la clase persona tiene los sigientes datos:: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es:{self.args},los datos importantes son :{self.wkargs}')


persona1 = Persona('ariel', 'betancud', 14142446884, 40)# necesitamos enviar argumentos
print(f'el objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}su edad es: {persona1.edad}')# tarea echa
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)

persona2 = Persona('osvaldo', 'giordanini',45455514, 45)
print(f'el objeto2 de la clase persoan: {persona2.nombre} {persona2.apellido} su edad es:  {persona2.edad}')

persona1.nombre = 'liliana'
persona1.apellido = 'bucella'
persona1.edad = 40
print(f'el objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido}su edad es: {persona1.edad}')

# los atributos son: caracteristicas
#los metodos son : el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) # debemos pasarle una referencia para el sef o dara error
persona1.telefono = '46018527410'
print(f'este es el telefono: {persona1.nombre} {persona1.telefono}')# hemos creado un atributo de un objeto


#print(persona2.telefono) # el objeto persona2 no tiene este atributo, da error
persona3 = Persona('rogelio' , 'romero',45747884785, 22, 'telefono', '2424220562', 'calle lopez ',575, 'manzana',77, 'casa',12, Altura=1.83,Peso=105, CFavorito='azul',Auto='citroen',modelo=2021)
persona3.mostrar_detalle()
#print(persona3.dni)# esto no se debe utilizar en python, esto dice que lo desconocemos
#persona3.__nombre # esta totalmente encapsulado