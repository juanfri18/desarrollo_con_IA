temperaturas = [18, 22, 19, 25, 30, 17, 28, 24]

mayores_20 = []
for t in temperaturas:
    if t >= 20:
        mayores_20.append(t)

diccionario = {}
contador = 0
for valor in mayores_20:
    diccionario[contador] = valor
    contador += 1

primeras_3 = temperaturas[:3]

print(mayores_20)
print(diccionario)
print(primeras_3)
