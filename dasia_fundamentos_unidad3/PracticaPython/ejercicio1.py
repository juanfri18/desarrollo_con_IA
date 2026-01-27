ventas = [15000, 18000, 22000, 17000, 25000, 30000, 28000, 32000, 27000, 29000, 35000, 40000]

print(" APARTADO A ")
# Uso la función sum() para el total
total_anual = sum(ventas)
print(f"Total de ventas del año: {total_anual} euros")

print("\n APARTADO B ")
def calcular_estadisticas(lista):
    # Calculo los datos básicos
    total = sum(lista)
    promedio = total / len(lista)
    
    # Busco el valor máximo y mínimo
    maximo_valor = max(lista)
    minimo_valor = min(lista)
    
    # Busco en qué posición (índice) están esos valores
    mes_mejor = lista.index(maximo_valor)
    mes_peor = lista.index(minimo_valor)
    
    return (total, promedio, mes_mejor, mes_peor)

# Llamo a la función y guardo el resultado
mis_stats = calcular_estadisticas(ventas)
print(f"Estadísticas: {mis_stats}")

print("\n APARTADO C ")
# Uso list comprehension para filtrar
promedio_actual = mis_stats[1]

# Uso enumerate para tener el índice y el valor a la vez
ventas_superiores = [f"Mes {i}: {v}€" for i, v in enumerate(ventas) if v > promedio_actual]

for mensaje in ventas_superiores:
    print(mensaje)

print("\n APARTADO D  ")
# Paso 1: Aplico el aumento del 15% con map
ventas_con_inflacion = list(map(lambda x: x * 1.15, ventas))

# Paso 2: Filtro las mayores a 30.000
ventas_altas = list(filter(lambda x: x > 30000, ventas_con_inflacion))

print("Ventas con inflación mayores a 30.000:")
print(ventas_altas)