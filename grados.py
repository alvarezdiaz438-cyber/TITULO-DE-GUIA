#convertir grados celsius a fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius=float(input("ngrese la temperatura es grados celsius: "))
resultado=celsius_a_fahrenheit(celsius)
print(f"la temperatura en grados fahrenheit es: {resultado}")
