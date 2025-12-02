#calcular el area de un cuadrado con el lado dado
def area_cuadrado(lado):
    area = lado ** 2
    return area
lado = float(input("ingrese el lado del cuadrado: "))
resultado = area_cuadrado(lado)
print(f"el area del cuadrado es: {resultado}")
