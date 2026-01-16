import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# a) Primer elemento
print(f"a) Primer elemento: {arr[0]}")


# b) Último elemento
print(f"b) Último elemento: {arr[-1]}")


# c) Elementos del índice 2 al 5 (el límite superior es exclusivo)
print(f"c) Índice 2 a 5: {arr[2:5]}")

# d) Desde índice 5 hasta el final
print(f"d) Índice 5 al final: {arr[5:]}")


# e) Desde el inicio hasta índice 4 (exclusivo)
print(f"e) Inicio hasta índice 4: {arr[:4]}")

# f) Elementos en posiciones pares (step de 2)
print(f"f) Posiciones pares: {arr[::2]}")

# g) Array invertido (step negativo)
print(f"g) Invertido: {arr[::-1]}")


