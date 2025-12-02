#determinar el volumen de un prisma tringular con la longitud de la base, altura y ancho especificados
def volumen_prisma_triangular(longitud_base, altura_triangulo, ancho_prisma):
    area_base = (longitud_base * altura_triangulo) / 2
    volumen = area_base * ancho_prisma
    return volumen
longitud_base = float(input("ingrese la longitud de la base del triangulo: "))
altura_triangulo = float(input("ingrese la altura del triangulo: "))
ancho_prisma = float(input("ingrese el ancho del prisma: "))
resultado = volumen_prisma_triangular(longitud_base, altura_triangulo, ancho_prisma)
print(f"el volumen del primsa triangular es: {resultado}")
