def capturar_datos():
    precio=float(input("digite precio del producto"))
    return precio

def procesar(precio):
    descuento=precio * 10 /100
    return descuento

def mostrar(descuento):
    print("el descuento es:",descuento)

precio= capturar_datos()
descuento=procesar(precio)
mostrar (descuento)
