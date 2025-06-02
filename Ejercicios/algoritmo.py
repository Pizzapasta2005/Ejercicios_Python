# operaciones_complejas.py

def ejecutar_operaciones_complejas():
    print("====== CALCULADORA CON NÚMEROS COMPLEJOS ======\n")

    try:
        # Entrada de datos
        num_entero = int(input("1. Ingresa un número entero: "))
        num_flotante = float(input("2. Ingresa un número flotante (decimal): "))
        entrada_compleja = input("3. Ingresa un número complejo (formato: a+bj, por ejemplo 2+3j): ")
        num_complejo = complex(entrada_compleja)
    except ValueError:
        print("\n[Error] Uno o más valores ingresados no son válidos. Verifica el formato.")
        return

    # Cálculos
    potencia_compleja = num_complejo ** num_entero
    suma_mixta = num_complejo + num_flotante
    producto_mixto = num_complejo * num_entero
    modulo_potencia = abs(potencia_compleja)

    # Resultados
    print("\n========== RESULTADOS ==========")
    print(f"A. Número complejo: {num_complejo}")
    print(f"B. Entero: {num_entero}")
    print(f"C. Flotante: {num_flotante}")

    print("\n--- Operaciones Realizadas ---")
    print(f"1. Potencia (complejo ^ entero): {potencia_compleja}")
    print(f"2. Suma (complejo + flotante): {suma_mixta}")
    print(f"3. Producto (complejo * entero): {producto_mixto}")
    print(f"4. Módulo de la potencia: {modulo_potencia:.3f}")

    print("\n✔ Operaciones completadas correctamente.\n")

# Punto de entrada principal
if __name__ == "__main__":
    ejecutar_operaciones_complejas()