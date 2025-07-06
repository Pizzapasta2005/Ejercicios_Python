
#Definir numeros (valores)

# Lista para guardar los valores
lista_numeros = []
total = 0

# incrementamos de 3 en 3 los numeros de rango mayor o igual a 500 a 100
numero = 500
while numero >= 100:
    print(numero)
    lista_numeros.append(numero)
    total += numero
    numero -= 3

# Ahora calculamos el promedio
cantidad = len(lista_numeros)
media = total / cantidad

# por ultimo mostramos los resultados finales
print("\nResultado de la suma:", total)
print("Promedio de los valores:", media)
