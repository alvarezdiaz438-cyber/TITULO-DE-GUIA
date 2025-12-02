#desarrola un programa que pida un numero de horas y lo convierta a minutos utlizando operadores aritmeticos
def convertir_horas_a_minutos(horas):
    minutos = horas * 60
    return minutos
horas = float(input("ingrese el numero de horas: "))
resultado = convertir_horas_a_minutos(horas)
print(f"el numero de minutos es: {resultado}")
