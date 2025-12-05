def capturar_datos():
    dinero = float(input("Digite la cantidad de dinero en la cuenta"))
    return dinero

def procesar(dinero):
    interes = dinero * 5/100
    return interes

def mostrar(dinero, interes):
    print("El interés del 5% es:",interes)
    print("Total con interés:",dinero+interes )

dinero = capturar_datos()
interes = procesar(dinero)
mostrar(dinero, interes)