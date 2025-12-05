def capturar_datos():
    num1 = float(input("ingrese el primer número: "))
    num2 = float(input("ingrese el segundo número: "))
    return num1, num2
def procesar(num1, num2):
    promedio = (num1 + num2) / 2
    return promedio
def mostrar(promedio):
    print("el promedio de los dos números es:", promedio)

num1,num2=capturar_datos()
promedio=procesar(num1, num2)
mostrar(promedio)