#desarrola un programa que requiera dos numeros y muestre el producto de dichos valores
def multiplicar_numeros(num1, num2):
    producto = num1 * num2
    return producto
numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))
resultado = multiplicar_numeros(numero1, numero2)
print(f"el producto de los dos numeros es: {resultado}")