def capturar_datos():
    numero1 = float(input("Digite el primer número "))
    numero2 = float(input("Digite el segundo número"))
    return numero1, numero2

def procesar(numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2

def mostrar(numero1, numero2, mayor):
    print(f"El mayor entre {numero1} y {numero2} es: {mayor}")

numero1, numero2 = capturar_datos()
mayor = procesar(numero1, numero2)
mostrar(numero1, numero2, mayor)