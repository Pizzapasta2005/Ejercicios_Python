# Crear el diccionario con frutas y sus precios del día
fruteria = {
    "Manzana": (800, 820, 790),
    "Platano": (600, 600, 580),
    "Cereza": (1500, 1480, 1520)
}

# Eliminar precios repetidos del plátano usando set
precios_unicos_platano = list(set(fruteria["Platano"]))

# Obtener lista con los nombres de todas las frutas
nombres_frutas = list(fruteria.keys())

# Calcular el promedio de los precios únicos del plátano
promedio_precio_platano = sum(precios_unicos_platano) / len(precios_unicos_platano)

# Mostrar resultados
print("=== Inventario de la Frutería ===")
for fruta, precios in fruteria.items():
    print(f"{fruta}: {precios}")

print("\n>> Precios únicos registrados para el plátano:", precios_unicos_platano)
print(">> Frutas disponibles hoy:", nombres_frutas)
print(f">> Precio promedio del plátano (sin repetir), con 3 decimales: {promedio_precio_platano:.3f}")
