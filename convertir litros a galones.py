#convertir litros a galones
def litros_a_galones(litros):
    galones = litros / 3.78541
    return galones
litros = float(input("ingrese la cantidad en litros: "))
resultado = litros_a_galones(litros)
print(f"la cantidad en galones es: {resultado}")
