# Conversor de Temperaturas: Celsius a Fahrenheit y Kelvin

def convertir_temperaturas():
    # Solicitar al usuario una temperatura en Celsius
    try:
        grados_celsius = float(input("Ingresa la temperatura en Celsius: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        return

    # Realizar las conversiones
    grados_fahrenheit = (grados_celsius * 1.8) + 32
    grados_kelvin = grados_celsius + 273.15

    # Mostrar los resultados con 2 decimales
    print("\nResultados de la conversión:")
    print(f"- Celsius: {grados_celsius:.2f} °C")
    print(f"- Fahrenheit: {grados_fahrenheit:.2f} °F")
    print(f"- Kelvin: {grados_kelvin:.2f} K")

# Ejecutar la función
convertir_temperaturas()
