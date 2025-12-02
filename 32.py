#diseña un algoritmo que calcule el area de un rectangulo, solicitando su longitud y su ancho
def area_rectangulo(longitud, ancho):
    area = longitud * ancho
    return area
longitud = float(input("ingrese la longitud del rectangulo: "))
ancho = float(input("ingrese el ancho del rectangulo: "))
resultado = area_rectangulo(longitud, ancho)
print(f"el area del rectangulo es: {resultado}")