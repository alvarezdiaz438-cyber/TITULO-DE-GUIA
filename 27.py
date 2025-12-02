#desarrole un programa que pida un numero y desarrolle su riaz cuadrada utilizando operadores aritmeticos
import math
def calcular_raiz_cuadrada(numero):
    raiz_cuadrada = math.sqrt(numero)
    return raiz_cuadrada
numero = float(input("ingrese un numero: "))
resultado = calcular_raiz_cuadrada(numero)
print(f"la raiz cuadrda del numero es: {resultado}")