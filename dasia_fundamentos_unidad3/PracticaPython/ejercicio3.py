import numpy as np

np.random.seed(42)
# Creo la matriz: 5 filas  y 7 columnas 
temperaturas = np.random.uniform(15, 35, size=(5, 7))

print(" APARTADO A  ")
print(f"Forma del array: {temperaturas.shape}")
print(f"Media global: {np.mean(temperaturas):.2f}")
print(f"Máxima: {np.max(temperaturas):.2f}")
print(f"Mínima: {np.min(temperaturas):.2f}")

print("\n APARTADO B  ")
# Calculo la media por filas 
media_por_sensor = np.mean(temperaturas, axis=1)
print(f"Media por sensor: {media_por_sensor}")

# Calculo la media por columnas 
media_por_dia = np.mean(temperaturas, axis=0)
print(f"Media por día: {media_por_dia}")

# Busco el índice del sensor con mayor media
mejor_sensor = np.argmax(media_por_sensor)
print(f"El sensor con mayor media es el índice: {mejor_sensor}")

print("\n APARTADO C ")
# Creo una máscara para valores > 28
mascara_calor = temperaturas > 28
cantidad_ajustes = np.sum(mascara_calor)

# Reemplazo valores usando la máscara
temperaturas[mascara_calor] = 28
print(f"Ajusté {cantidad_ajustes} valores al límite de 28.")

print("\n APARTADO D   ")
# Normalizo los datos con la fórmula Min-Max
valor_min = np.min(temperaturas)
valor_max = np.max(temperaturas)
datos_normalizados = (temperaturas - valor_min) / (valor_max - valor_min)

print("Primeras 3 filas normalizadas:")
print(datos_normalizados[:3])

print("\n--- APARTADO E ---")
# Defino las alertas para cada sensor
alertas = np.array([10, 20, 15, 25, 18])

# Redimensiono el array a columna (5,1) para poder sumarlo a la matriz
alertas_vertical = alertas.reshape(5, 1)

resultado_final = temperaturas + alertas_vertical
print("Forma final tras sumar alertas:", resultado_final.shape)
print("Ejemplo fila 0 sumada:", resultado_final[0])