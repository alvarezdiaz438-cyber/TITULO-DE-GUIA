#determinar el volumen de un cono
def volumen_cono(radio, altura):
    volumen = (1/3) * 3.1416 * (radio**2) * altura
    return volumen
radio = float(input("ingrese el radio de la base del cono: "))
input_altura = float(input("ingrese la altura del cono: "))
resultado = volumen_cono(radio, input_altura)
print(f"el volumen del cono es: {resultado}")
