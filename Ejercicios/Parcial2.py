#Comenzamos por crear un diccionario con sus claves siendo su numero de ingreso y con sub-diccionarios con claves como nombre, peso, edad y tamaño.



VeterinariaGatitos = {
    "101":{
        "Nombre": "Luna",
        "Peso" : float(1.2),
        "Edad" : "3 meses",
        "Tamaño": 30},
     "102":{
        "Nombre":"Michi",
        "Peso":float(0.8),
        "Edad":"2 meses",
        "Tamaño":25},
     "103":{
        "Nombre":"Pepito",
        "Peso":float(2.5),
        "Edad":"5 meses",
        "Tamaño":35
     }
}
print(VeterinariaGatitos)

for Peso in VeterinariaGatitos:
    if Peso => 1:
        print("Peso Bajo"),
    elif Peso > 1 < 4:
        print("Peso Normal"),
    else: print("Sobre Peso")
#ahora recorremos el diccionario con un bucle y añadimos la clave "Clasificacion Peso"


    
    
