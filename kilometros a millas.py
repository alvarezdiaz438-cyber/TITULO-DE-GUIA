#hola mundo py
def kilometros_a_millas(kilometros):
    millas = kilometros * 0.621371
    return millas
#convertir millas a kilometros
def millas_a_kilometros(millas):
 kilometros = millas / 0.621371
 return kilometros
#ejemplo de uso
distancia_km = 10
distancia_millas = kilometros_a_millas(distancia_km)
print(f"{distancia_km} kilometros son {distancia_millas} millas.")
distancia_millas = 6.21371
distancia_km = millas_a_kilometros(distancia_millas)
print(f"{distancia_millas} millas son {distancia_km} kilometros.")
