"""

Dado dos diccionarios 1 de productos y el 2 de categoría, conocer un 3 que permita tener el nombre 
del producto y el nombre de su categoría ejemplo.

"""

#SOLUCIÓN
productos=[
    {
        "id": 123,
        "nombre": "Libreta",
        "precio": 12.500,
        "id_cat": 1
    },
    {
        "id": 111,
        "nombre": "Jabon ",
        "precio": 10.500,
        "id_cat": 2
    }
]
categorias=[
    {
        "id": 1,
        "nombre": "Utiles escolares",
    },
    {
        "id": 2,
        "nombre": "Aseo ",
    }
]

resultado= []

for produ in productos:
    for cate in categorias:
        if produ["id_cat"] == cate["id"]:
            resultado.append({
                "id": produ["id"],
                "nombre_producto": produ["nombre"],
                "nombre_categoria": cate["nombre"]
            })

for resul in resultado:
    print(f"ID: {resul['id']} - Producto: {resul['nombre_producto']} - Categoría: {resul['nombre_categoria']}")
