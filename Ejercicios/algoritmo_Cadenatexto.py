# archivo: analisis_texto.py

def es_frase_valida(texto, max_caracteres=30):
    """
    Verifica si la frase ingresada cumple con el límite de caracteres permitido.
    """
    return len(texto) <= max_caracteres

def contar_apariciones(frase, letra_objetivo):
    """
    Cuenta cuántas veces aparece una letra determinada en la frase,
    sin diferenciar entre mayúsculas y minúsculas.
    """
    cantidad = 0
    for letra in frase:
        if letra.lower() == letra_objetivo.lower():
            cantidad += 1
    return cantidad

def mostrar_informacion(frase):
    """
    Genera y muestra un análisis detallado de la frase ingresada.
    """
    print("\n========== RESULTADO DEL ANÁLISIS ==========\n")

    # Transformaciones de la frase
    frase_en_mayusculas = frase.upper()
    frase_en_minusculas = frase.lower()
    longitud = len(frase)
    cantidad_a = contar_apariciones(frase, 'a')

    # Salida detallada
    print(f"Frase original:        {frase}")
    print(f"Frase en mayúsculas:   {frase_en_mayusculas}")
    print(f"Frase en minúsculas:   {frase_en_minusculas}")
    print(f"Longitud de la frase:  {longitud} caracteres")
    print(f"Número de letras 'a' o 'A': {cantidad_a}")
    
    if cantidad_a == 0:
        print("La letra 'a' no se encuentra en la frase.")
    elif cantidad_a == 1:
        print("La letra 'a' aparece una sola vez.")
    else:
        print(f"La letra 'a' aparece {cantidad_a} veces en total.")

    print("\n✔ Análisis finalizado con éxito.\n")

def main():
    print("====== ANALIZADOR DE FRASES ======\n")
    print("Este programa analiza una frase corta y realiza distintas operaciones sobre ella.\n")
    
    # Entrada del usuario
    frase_usuario = input("Por favor, ingresa una frase de máximo 30 caracteres:\n→ ")

    # Validación de longitud
    if not es_frase_valida(frase_usuario):
        print("\n[ERROR] La frase supera el límite de 30 caracteres permitidos.")
        print("Intenta de nuevo con una frase más corta.")
        return

    # Procesamiento y salida
    mostrar_informacion(frase_usuario)

# Ejecutar si es archivo principal
if __name__ == "__main__":
    main()