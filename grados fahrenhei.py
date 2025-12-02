#convertir grados celsius a farenheit
def celsius_a_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit
#convertir grados farenheit a celsius
def farenheit_a_celsius(farenheit):
    celsius = (farenheit - 32) * 5/9
    return celsius
#ejemplo de uso
temp_celsius = 25
temp_farenheit = celsius_a_farenheit(temp_celsius)
print(f"{temp_celsius} grados celsius son {temp_farenheit} grados farenheit.")
temp_farenheit = 77
temp_celsius = farenheit_a_celsius(temp_farenheit)
print(f"{temp_farenheit} gradosfarenheit son {temp_celsius} grados celsius.")
