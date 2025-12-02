#crea un algoritmo que determine el residuo de la division entre dos numeros ingresados por el usuario
def calcular_residuo(num1, num2):
    residuo = num1 % num2
    return residuo
numero1= float(input("ingrese el primer numero: "))
numero2= float(input("ingrese el segundo numero: "))
resultado = calcular_residuo(numero1, numero2)
print(f"el residuo de la division entre los dos numeros es: {resultado}")