#area de un paralelogramo
def area_paralelogramo(base, altura):
    area = base * altura
    return area
base=float(input("ingrese la base del paralelogramo: "))
altura=float(input("ingrese la altura del paralelogramo: "))
resultado=area_paralelogramo(base, altura)
print(f"el area del paralelogramo es: {resultado}")
