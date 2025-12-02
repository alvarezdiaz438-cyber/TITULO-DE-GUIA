#crea un algoritmo que solocite el radio de un circulo y calcule su circunferencia
import math
def calcular_circunferencia(radio):
    circunferencia = 2*math.pi*radio
    return circunferencia
radio = float(input("ingrese el radio del circulo: "))
resultado = calcular_circunferencia(radio)
print(f"la circunferencia del circulo es: {resultado}")
