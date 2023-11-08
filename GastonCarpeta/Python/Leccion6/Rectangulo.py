class Aritmetica:
    """
    crear una clase llamada rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular area utilizano la formula:
    area = base * altura. pero la base y la altura deben ser ingresadas por el usuari y los objetos deben ser tres.
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura

base = int(input('digite el numero para la base del rectangulo:'))
altura = int(input('digite el numero para la altura del rectangulo: '))
rectangulo1 = Rectangulo(base, altura)
print(f'el area del rectangulo es: {rectangulo1.calcular_area()}')