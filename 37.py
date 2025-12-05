def capturar_datos():
    numero1 = int(input("Digite el primer número: "))
    numero2 = int(input("Digite el segundo número: "))
    return numero1, numero2

def procesar(numero1, numero2):
    if numero1 % numero2 == 0:
        return f"{numero1} es múltiplo de {numero2}"
    else:
        return f"{numero1} NO es múltiplo de {numero2}"

def mostrar(mensaje):
    print(mensaje)

numero1, numero2 = capturar_datos()
mensaje = procesar(numero1, numero2)
mostrar(mensaje)