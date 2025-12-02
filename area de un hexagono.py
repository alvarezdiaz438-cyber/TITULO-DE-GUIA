#calcular el area de un hexagono regular con su lado dado
def area_hexagono(lado):
    area = (3 * (3 ** 0.5) * (lado ** 2)) / 2
    return area
lado = float(input("ingrese el lado del hexagono: "))
resultado = area_hexagono(lado)
print(f"el area del hexagono es: {resultado}")
