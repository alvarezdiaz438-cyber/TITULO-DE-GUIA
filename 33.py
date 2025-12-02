#crea un algoritmo que solicite una distancia en kilometros y la convierta a millas
def convertir_kilometros_a_millas(kilometros):
    millas = kilometros * 0.621371
    return millas
kilometros = float(input("ingrese la distancia en kilometros: "))
resultado = convertir_kilometros_a_millas(kilometros)
print(f"la distancia en millas es: {resultado}")