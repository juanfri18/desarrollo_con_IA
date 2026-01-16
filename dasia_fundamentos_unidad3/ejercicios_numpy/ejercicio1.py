import numpy as np

# a) Array del 0 al 9
arr_a = np.arange(10)

# b) Array 3x4 de ceros
arr_b = np.zeros((3, 4))

# c) Array 2x5 de unos
arr_c = np.ones((2, 5))

# d) Matriz identidad 4x4
arr_d = np.eye(4)

# e) Explorar propiedades de cada array

#arr_a
print("--- Array 0-9 ---")
print(f"Forma (shape): {arr_a.shape}")
print(f"Dimensiones (ndim): {arr_a.ndim}")
print(f"Tamaño total (size): {arr_a.size}")
print(f"Tipo de datos (dtype): {arr_a.dtype}")
print() # Salto de línea estético

#arr_b
print("--- Array Ceros ---")
print(f"Forma (shape): {arr_b.shape}")
print(f"Dimensiones (ndim): {arr_b.ndim}")
print(f"Tamaño total (size): {arr_b.size}")
print(f"Tipo de datos (dtype): {arr_b.dtype}")
print()

#arr_c
print("--- Array Unos ---")
print(f"Forma (shape): {arr_c.shape}")
print(f"Dimensiones (ndim): {arr_c.ndim}")
print(f"Tamaño total (size): {arr_c.size}")
print(f"Tipo de datos (dtype): {arr_c.dtype}")
print()

#arr_d
print("--- Matriz Identidad ---")
print(f"Forma (shape): {arr_d.shape}")
print(f"Dimensiones (ndim): {arr_d.ndim}")
print(f"Tamaño total (size): {arr_d.size}")
print(f"Tipo de datos (dtype): {arr_d.dtype}")