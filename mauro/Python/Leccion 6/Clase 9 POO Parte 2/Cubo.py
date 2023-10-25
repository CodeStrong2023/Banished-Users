class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad con
    un método calcular_volumen que tendrá la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    """
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad
    # Método para calcular volumen
    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad
    
# Datos a pedir
ancho = int(input('Digite el ancho: '))
altura = int(input('Digite la altura: '))
profundidad = int(input('Digite la profundidad: '))

cubo1 = Cubo(ancho,altura,profundidad)
print(f'El Volumen de los datos ingresados es: {cubo1.calcular_volumen()} ')
