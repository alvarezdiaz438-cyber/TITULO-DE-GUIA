#calcular el area de un trapecio
def area_trapecio(base_mayor, base_menor, altura):
    area=((base_mayor + base_menor) * altura) / 2
    return area
base_mayor = float(input("ingrese la base mayor del trapecio: "))
input_base_menor = float(input("ingrese la base menor del trapecio: "))
altura = float(input("ingrese la altura del trapecio: "))
resultado = area_trapecio(base_mayor, input_base_menor, altura)
print(f"el area del trapecio es: {resultado}")
