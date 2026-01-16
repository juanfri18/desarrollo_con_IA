import numpy as np

temperaturas = np.array([18, 22, 25, 19, 30, 15, 28, 23, 17, 31, 20, 26])

# a) Máscara > 25 
mascara_calor = temperaturas > 25
print(f"Máscara > 25: {mascara_calor}")

# b) Filtrar temperaturas > 25 
print(f"Temperaturas filtradas: {temperaturas[mascara_calor]}")

# c) Contar temperaturas > 25 
print(f"Cantidad > 25: {np.sum(mascara_calor)}")

# d) Máscara entre 20 y 25 
mascara_templada = (temperaturas >= 20) & (temperaturas <= 25)
print(f"Temperaturas templadas: {temperaturas[mascara_templada]}")

# e) Reemplazar valores > 28 con 28 
temp_seguras = temperaturas.copy() 
temp_seguras[temp_seguras > 28] = 28
print(f"Temperaturas limitadas: {temp_seguras}")

# f) Clasificar temperaturas 
condiciones = [
    temperaturas < 20,
    (temperaturas >= 20) & (temperaturas <= 25),
    temperaturas > 25
]
etiquetas = ["Frío", "Templado", "Calor"]
clasificacion = np.select(condiciones, etiquetas)
print(f"Clasificación: {clasificacion}")