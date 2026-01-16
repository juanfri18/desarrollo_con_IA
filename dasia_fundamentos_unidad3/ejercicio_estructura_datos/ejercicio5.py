grupo_a = {"Ana", "Carlos", "Elena", "David", "Beatriz"}
grupo_b = {"Carlos", "Elena", "Fernando", "Gloria"}

# 1. Estudiantes en ambos grupos
ambos = grupo_a & grupo_b

# 2. Solo en grupo A
solo_a = grupo_a - grupo_b

# 3. Total sin repetir
total = grupo_a | grupo_b
cantidad_total = len(total)

# 4. Elimina duplicados de una lista
lista = [1, 2, 2, 3, 4, 4, 4, 5]
sin_duplicados = list(set(lista))

print(ambos)
print(solo_a)
print(cantidad_total)
print(sin_duplicados)
