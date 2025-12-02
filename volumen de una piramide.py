#volumen de una piramide
def volumen_piramide(longitud_base, ancho_base, altura):
    volumen = (longitud_base * ancho_base * altura) / 3
    return volumen
longitud_base = float(input("ingrese la longitud de la base de la piramide: "))
ancho_base = float(input("ingrese el ancho de la base de la piramide: "))
altura = float(input("ingrese la altura de la piramide: "))
resultado = volumen_piramide(longitud_base, ancho_base, altura)
print(f"el volumen de la piramide es: {resultado}")