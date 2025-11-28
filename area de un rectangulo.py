#area del rectangulo
def area_rectangulo(longitud, ancho):
    area=longitud*ancho
    return area
longitud=float(input("ingrese la longitud del rectangulo: "))
ancho=float(input("ingrese el ancho del rectangulo: "))
resultado=area_rectangulo(longitud, ancho)
print(f"el area del rectangulo es: {resultado}")
