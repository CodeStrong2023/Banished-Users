class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    esto es documentación de la clase python
    En esta clase: algunas operaciones de suma, resta, multiplicación y mas
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    # Método para sumar
    def sumar(self):
        return self.operandoA + self.operandoB
    # Método para restar
    def restar(self):
        return self.operandoA - self.operandoB
    # Método para multiplicar
    def multiplicar(self):
        return self.operandoA * self.operandoB
    # Metodo para dividir
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7, 9) # Le pasamos los argumentos para los operandos
print(f'La suma de los números es: {aritmetica1.sumar()}')
print(f'La resta de los números es: {aritmetica1.restar()}')
print(f'La multiplicación de los números es: {aritmetica1.multiplicar()}')
print(f'La division de los números es: {aritmetica1.dividir():.2f}') # :.2f = Solo muestre dos num flotantes despues de la ,