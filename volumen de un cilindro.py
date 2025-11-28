#volumen de un cilindro
def volumen_cilindro(radio, altura):
    volumen = 3.1416 * (radio**2) * altura
    return volumen
radio = float(input("ingrese el radio de la base del cilindro: " ))
altura = float(input("ingrese la altura del clindro:"))
resultado = volumen_cilindro(radio, altura)
print(f"el voluen del cilindro es: {resultado}") 

