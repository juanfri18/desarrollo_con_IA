# Dada esta lista de precios en euros:
# Usa map() para:
# 1. Convertir a dólares (multiplica por 1.1)
# 2. Redondear a 2 decimales con round()
# Imprime la lista resultante
precios_euros = [19.99, 49.99, 12.50, 99.99, 5.00]
def convertir_a_dolares(c):
    numero=round((c*1.1),2)
    return print(numero)

precios_dolares =list(map(convertir_a_dolares,precios_euros))

