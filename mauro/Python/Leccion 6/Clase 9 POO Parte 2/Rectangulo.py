class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tenér dos atributos: altura y base
    el nombre del método sera calcular area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresados por
    el usuario y los objetos deben ser tres.
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    # Método para calcular el area
    def calcular_area(self):
        return self.base * self.altura
    
# Se piden datos al usurario
base = int(input('Digite el número para la BASE del rectangulo: '))
altura = int(input('Digite el número para la ALTURA del rectangulo: '))
rectangulo1 = Rectangulo(base, altura) # Se asigna el objeto

print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')