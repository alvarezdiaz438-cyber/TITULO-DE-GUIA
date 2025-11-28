# Volumen de una esfera con su radio dado
radio = float(input("Ingrese el radio de la esfera: "))

def volumen_esfera(r):
    volumen = (4/3) * 3.1416 * (r**3)
    return volumen

resultado = volumen_esfera(radio)
print(f"El volumen de la esfera es: {resultado}")