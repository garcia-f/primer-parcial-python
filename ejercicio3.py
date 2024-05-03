import pandas as pd


productos = [
{"nombre": "Camiseta", "precio": 20, "cantidad_disponible":
100},
{"nombre": "Pantalón", "precio": 30, "cantidad_disponible": 80},
{"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
{"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
{"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
{"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
{"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
{"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
{"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
{"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible":
25},
{"nombre": "Calcetines", "precio": 10, "cantidad_disponible":
150},
{"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
{"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
{"nombre": "Pendientes", "precio": 15, "cantidad_disponible":
180},
{"nombre": "Cinturón", "precio": 20, "cantidad_disponible":
100},
{"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
{"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
{"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
{"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
{"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
]



# Calcular el valor total del inventario (precio * cantidad_disponible) para cada producto y mostrarlo.
for _, x in enumerate(productos):
    valor_productos = []
    valor = x["precio"] * x["cantidad_disponible"]
    valor_productos.append(f"producto: {x["nombre"]}")
    valor_productos.append(f"valor total: {valor}")
    # print(valor_productos)

# Calcular el valor total del inventario sumando el valor total de cada producto.
valor_total_inventario = 0
for _, x in enumerate(productos):
    valor = x["precio"] * x["cantidad_disponible"]
    valor_total_inventario += valor
# print(f"El valor total del inventario es {valor_total_inventario}")


# Crear un DataFrame que incluya dos columnas una para los nombres de los productos y otra para la cantidad disponible de cada producto
df = pd.DataFrame(productos)
df.drop('precio', axis=1, inplace=True)
# print(df)