# ejercicio2.py

productos = {
    "laptop": {"precio": 850, "stock": 15, "categoria": "informatica"},
    "raton": {"precio": 25, "stock": 50, "categoria": "informatica"},
    "teclado": {"precio": 45, "stock": 30, "categoria": "informatica"},
    "monitor": {"precio": 200, "stock": 20, "categoria": "informatica"},
    "silla": {"precio": 150, "stock": 10, "categoria": "mobiliario"},
    "mesa": {"precio": 300, "stock": 5, "categoria": "mobiliario"}
}

print(" APARTADO A  ")
def valor_total_inventario(diccionario_productos):
    total = 0
    # Recorro solo los valores 
    for info in diccionario_productos.values():
        precio = info["precio"]
        cantidad = info["stock"]
        total = total + (precio * cantidad) 
    return total

print(f"Valor total del inventario: {valor_total_inventario(productos)}€")

print("\n APARTADO B")
def productos_por_categoria(diccionario, categoria_buscada):
    nuevo_diccionario = {}
    # Recorro nombre y datos 
    for nombre, datos in diccionario.items():
        if datos["categoria"] == categoria_buscada:
            nuevo_diccionario[nombre] = datos
    return nuevo_diccionario

muebles = productos_por_categoria(productos, "mobiliario")
print(f"Productos de mobiliario: {muebles}")

print("\n APARTADO C ")
bajo_stock = {nombre: datos["stock"] for nombre, datos in productos.items() if datos["stock"] < 20} 
print(f"Productos con poco stock: {bajo_stock}")

print("\n APARTADO D  ")
def actualizar_precios(diccionario, porcentaje):
    lista_caros = []
    factor = 1 + (porcentaje / 100)
    
    for nombre, datos in diccionario.items():
        # Modifico el precio directamente en el diccionario original
        datos["precio"] = datos["precio"] * factor 
        
        # Compruebo si el nuevo precio supera 200
        if datos["precio"] > 200:
            lista_caros.append(nombre)
            
    return lista_caros

productos_caros = actualizar_precios(productos, 10)
print(f"Productos que ahora valen más de 200€: {productos_caros}")