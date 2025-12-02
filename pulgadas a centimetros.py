#pulgadas a centimetros
def pulgadas_a_centimetros(pulgadas):
    centimetros = pulgadas * 2.54
    return centimetros
#convertir centimetros a pulgadas
def centimetros_a_pulagadas(centimetros):
    pulgadas = centimetros / 2.54
    return pulgadas
#ejemplo de uso
distancia_pulgadas = 10
distancia_centimetros = pulgadas_a_centimetros(distancia_pulgadas)
print(f"{distancia_pulgadas} pulgadas son {distancia_centimetros} centimetros.")
distancia_centimetros = 25.4
distancia_pulgadas = centimetros_a_pulagadas(distancia_centimetros)
print(f"{distancia_centimetros} centimetros son {distancia_pulgadas} pulgadas.")