# Ejercicio 4: Calculadora de Impuestos
# Crear una función para calcular el total de un pago incluyendo un impuesto aplicado. (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxx

# Creamos la función para calcular el TOTAL del pago incluyendo el impuesto
def calcularTotalP(pagoSinImpuesto, impuesto):
    pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
    return pagoTotal

# Se ejecuta la función con datos del usuario
pagoSinImpuesto = float(input('Digite el pago sin impuestos: '))
impuesto = float(input('Digite el monto del impuesto aplicar: '))
pagoConImpuesto = calcularTotalP(pagoSinImpuesto, impuesto)

print(f'El pago con impuesto es: {pagoConImpuesto}')