#volumen de un cubo
def volumen_cubo(lado):
    volumen = lado ** 3
    return volumen
lado = float(input("ingrese la longitud del lado del cubo: "))
resultado = volumen_cubo(lado)
print(f"el volumen del cubo es: {resultado}")