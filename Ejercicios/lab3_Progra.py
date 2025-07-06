#A) Creamos el diccionario con sub diccionarios como valores que den la informacion de "Ciudad", "temperatura y "Precipitacion
# Diccionario original
clima_ciudades = {
    "5700000": {
        "Ciudad": "Castro",
        "Temperatura": 11,
        "Precipitación": 2000
    },
    "5770000": {
        "Ciudad": "Chonchi",
        "Temperatura": 8,
        "Precipitación": 2800
    },
    "5790000": {
        "Ciudad": "Quellon",
        "Temperatura": 10,
        "Precipitación": 2950
    }
}
# B) Ahora agregamos la clave "Clima" con condicionales, ademas se implementa una estructura de control de errores utiliando "try" y "except"
# Agregar la clave "Clima" con control de errores
for codigo_postal in clima_ciudades:
    try:
        temp = clima_ciudades[codigo_postal]["Temperatura"]
        
        if temp < 10:
            clima = "Frío"
        elif 10 <= temp <= 15:
            clima = "Templado"
        else:
            clima = "Cálido"
    
    except (KeyError, TypeError, ValueError):
        clima = "Desconocida"

    clima_ciudades[codigo_postal]["Clima"] = clima

# Imprimir el diccionario actualizado
for codigo, datos in clima_ciudades.items():
    print(f"Código Postal: {codigo}")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")
    print()





#C) Agregamos al subdiccionario de Castro una nueva clave de "Meses mas lluviosos" con una lista vacia y luego utilizamos un metodo en python para agregar los tres meses uno a uno en cada ciudad (Mayo, Junio y Julio) ademas de luego remover Junio con otro metodo

clima_ciudades["5700000"]["Meses Más Lluviosos"] = []
clima_ciudades["5770000"]["Meses Más Lluviosos"] = []
clima_ciudades["5790000"]["Meses Más Lluviosos"] = []
# Agregar meses uno a uno
clima_ciudades["5700000"]["Meses Más Lluviosos"].append("Mayo")
clima_ciudades["5700000"]["Meses Más Lluviosos"].append("Junio")
clima_ciudades["5700000"]["Meses Más Lluviosos"].append("Julio")

clima_ciudades["5770000"]["Meses Más Lluviosos"].append("Mayo")
clima_ciudades["5770000"]["Meses Más Lluviosos"].append("Junio")
clima_ciudades["5770000"]["Meses Más Lluviosos"].append("Julio")


clima_ciudades["5790000"]["Meses Más Lluviosos"].append("Mayo")
clima_ciudades["5790000"]["Meses Más Lluviosos"].append("Junio")
clima_ciudades["5790000"]["Meses Más Lluviosos"].append("Julio")



# Eliminar el segundo mes: "Junio"
clima_ciudades["5700000"]["Meses Más Lluviosos"].remove("Junio")
clima_ciudades["5770000"]["Meses Más Lluviosos"].remove("Junio")
clima_ciudades["5790000"]["Meses Más Lluviosos"].remove("Junio")
# Imprimir los datos de los resultados a mostrar
print("Datos de Castro:")
for clave, valor in clima_ciudades["5700000"].items():
    print(f"  {clave}: {valor}")

print("Datos de Chochi:")
for clave, valor in clima_ciudades["5770000"].items():
    print(f"  {clave}: {valor}")

print("Datos de Quellon:")
for clave, valor in clima_ciudades["5790000"].items():
    print(f"  {clave}: {valor}")


#D) Actualizamos el Valor de Chonchi Cambiandolo por "Ciudad de Tres Pisos"

clima_ciudades["5770000"].update({"Ciudad": "Ciudad de los Tres Pisos"})

# Imprimir los datos de Chonchi para verificar el cambio
print("Datos de Chonchi:")
for clave, valor in clima_ciudades["5770000"].items():
    print(f"  {clave}: {valor}")

#E) Creamos una lista llamada Lluvias 

lluvias = [
    clima_ciudades["5700000"]["Precipitación"],     # Castro
    clima_ciudades["5770000"]["Precipitación"],     # Ciudad de los Tres Pisos
    clima_ciudades["5790000"]["Precipitación"]      # Quellon
]

# Mostrar suma total de precipitaciones
suma_total = sum(lluvias)
print("Suma total de precipitaciones:", suma_total)

# Mostrar la mayor y menor precipitación
mayor = max(lluvias)
menor = min(lluvias)
print("Mayor precipitación:", mayor)
print("Menor precipitación:", menor)

# Mostrar índice (posición) de la precipitación más alta
indice_mayor = lluvias.index(mayor)
print("Índice de la precipitación más alta:", indice_mayor)