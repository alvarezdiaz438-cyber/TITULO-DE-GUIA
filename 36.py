def capturar_datos():
    numero1 = int(input("Digite el primer número entero "))
    numero2 = int(input("Digite el segundo número entero "))
    return numero1, numero2

def procesar(numero1, numero2):
    cociente = numero1 / numero2  
    return cociente

def mostrar( cociente):
    print("El cociente es:",cociente)

numero1, numero2 = capturar_datos()
cociente = procesar(numero1, numero2)
mostrar( cociente)