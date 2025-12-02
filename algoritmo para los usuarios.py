#crea un algoritmo que pida al usuario dos numeros y calcule la resta del primero menos el segundo
def restar_numeros(num1, num2):
    resta = num1 - num2
    return resta
numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))
resultado = restar_numeros(numero1, numero2)
print(f"la resta del primer numero menos el segundo es: {resultado}")