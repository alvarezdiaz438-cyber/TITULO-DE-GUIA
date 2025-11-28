#calcular el area de un circulo con su radio
def area_circulo(raddio):
    area=3.1416*(raddio**2)
    return area
radio=float(input("ingrese el radio del circulo: "))
resultado=area_circulo(radio)
print(f"el area del circulo es: {resultado}")
