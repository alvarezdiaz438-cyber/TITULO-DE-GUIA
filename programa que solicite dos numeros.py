#programa que solicite dos numeros
def sumar_numeros(num1, num2):
    suma = num1 + num2
    return suma
numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))
resultado = sumar_numeros(numero1, numero2)
print(f"la suma de los dos numeros es: {resultado}")
