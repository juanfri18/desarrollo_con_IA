import numpy as np

# a) Crear arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# b) Operaciones elemento a elemento
print(f"Suma: {a + b}")
print(f"Resta: {b - a}")
print(f"Multiplicación: {a * b}")
print(f"División: {b / a}")
print(f"Potencia (a²): {a ** 2}")

# c) Multiplicar por escalar 
print(f"a multiplicado por 10: {a * 10}")

# d) Sumar escalar
print(f"b más 100: {b + 100}")

# e) Raíz cuadrada
print(f"Raíz cuadrada de b: {np.sqrt(b)}")