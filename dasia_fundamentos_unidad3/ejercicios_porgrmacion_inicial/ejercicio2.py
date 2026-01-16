from functools import reduce
# Dada esta lista de calificaciones:
notas = [4.5, 7.0, 3.2, 8.5, 5.5, 9.0, 4.0, 6.5]

# Usa filter() para obtener solo las notas >= 5.0
# Luego usa map() para convertirlas a strings con formato "Nota: X.X"
def num_mayores_5(num):
    return num>=5
def cambio_format(num):
    return print(f"nota: {num}")
notas_mayorse_5= filter(num_mayores_5,notas)
formato_notas=list(map(cambio_format,notas_mayorse_5))
