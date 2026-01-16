import numpy as np

ventas = np.array([
    [1000, 1200, 1100, 1300],
    [900, 1000, 950, 1050],
    [1500, 1600, 1550, 1700]
])

# a) Shape
print(f"Forma de la matriz: {ventas.shape}")

# b) Ventas Tienda 2
print(f"Ventas Tienda 2: {ventas[1]}")

# c) Ventas Trimestre 3 
print(f"Ventas Trimestre 3: {ventas[:, 2]}")

# d) Total por tienda
total_tiendas = np.sum(ventas, axis=1)
print(f"Total por tienda: {total_tiendas}")

# e) Total por trimestre
total_trimestres = np.sum(ventas, axis=0)
print(f"Total por trimestre: {total_trimestres}")

# f) Media por tienda
print(f"Media por tienda: {np.mean(ventas, axis=1)}")

# g) Tienda con mayores ventas

idx_mejor_tienda = np.argmax(total_tiendas)
print(f"Tienda con mayores ventas {idx_mejor_tienda} (Tienda {idx_mejor_tienda + 1})")

# h) Trimestre con menores ventas 
idx_peor_trimestre = np.argmin(total_trimestres)
print(f" Trimestre con menores ventas {idx_peor_trimestre} (Trimestre {idx_peor_trimestre + 1})")