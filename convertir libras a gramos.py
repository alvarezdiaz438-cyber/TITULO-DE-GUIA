#convertir libras a gramos
def libras_a_gramos(libras):
    gramos = libras * 453.592
    return gramos
libras = float(input("ingrese la cantidad en libras: "))
resultado = libras_a_gramos(libras)
print(f"la cantidad en gramos es: {resultado}")
