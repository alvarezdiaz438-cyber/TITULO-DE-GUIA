#diseña un algoritmo que pida un numero y calcule su cuadro utilizando el operador de multiplicación
def calcular_cuadro(numero):
    cuadro = numero * numero
    return cuadro
numero = float(input("ingrese un numero: "))
resultado = calcular_cuadro(numero)
print(f"el cuadro del numero es: {resultado}")