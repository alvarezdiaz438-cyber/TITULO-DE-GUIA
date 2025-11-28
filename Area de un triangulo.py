#hola mundo de python
def area_triangulo(base, altura):
    area=(base*altura)/2
    return area
base=float(input("ingrese la base del triangulo: "))
altura=float(input("ingrese la altura del triangulo: "))
resultado=area_triangulo(base, altura)
print(f"el area del triangulo es: {resultado}")
