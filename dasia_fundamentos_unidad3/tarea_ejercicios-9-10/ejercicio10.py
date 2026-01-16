import string

# Lista de palabras comunes prohibidas
PALABRAS_PROHIBIDAS = [
    "password", "admin", "123456", "querty", "usuario", 
    "secret", "hola", "acceso", "root", "master",
    "fútbol", "familia", "amor", "dragon", "super"
]

def validar_password(password):
    errores = []
    
    # 1. Longitud mínima
    if len(password) < 12:
        errores.append("Longitud insuficiente (debe tener al menos 12 caracteres)")

    # Contadores
    mayusculas = 0
    minusculas = 0
    numeros = 0
    simbolos = 0
    
    caracteres_simbolos = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    for char in password:
        if char.isupper():
            mayusculas += 1
        elif char.islower():
            minusculas += 1
        elif char.isdigit():
            numeros += 1
        elif char in caracteres_simbolos:
            simbolos += 1

    # 2. Validar conteos
    if mayusculas < 2:
        errores.append(f"Faltan mayúsculas (tienes {mayusculas}, necesitas 2)")
    if minusculas < 2:
        errores.append(f"Faltan minúsculas (tienes {minusculas}, necesitas 2)")
    if numeros < 2:
        errores.append(f"Faltan números (tienes {numeros}, necesitas 2)")
    if simbolos < 2:
        errores.append(f"Faltan símbolos (tienes {simbolos}, necesitas 2)")

    # 3. Palabras comunes (Búsqueda insensible a mayúsculas/minúsculas)
    pass_lower = password.lower()
    for palabra in PALABRAS_PROHIBIDAS:
        if palabra in pass_lower:
            errores.append(f"No puede contener la palabra común: '{palabra}'")
            break # Si encuentra una, ya es inválida, no hace falta buscar más palabras

    # 4. Tres caracteres consecutivos iguales
    # Iteramos hasta len-2 para poder comparar i, i+1 y i+2 sin salirnos del rango
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            errores.append(f"Contiene caracteres repetidos consecutivos: '{password[i]*3}'")
            break

    # Retorno: True si la lista de errores está vacía, False si no + la lista
    es_valida = len(errores) == 0
    return es_valida, errores

# --- PRUEBAS ---

# Caso 1: Contraseña débil
p1 = "MiPass123!@"
valida1, errores1 = validar_password(p1)
print(f"\nProbando: '{p1}'")
print(f"Válida: {valida1}")
print("Errores:", errores1)

# Caso 2: Contraseña con repeticiones y palabra común
p2 = "SuperAdmin$$99aaa"
valida2, errores2 = validar_password(p2)
print(f"\nProbando: '{p2}'")
print(f"Válida: {valida2}")
print("Errores:", errores2)

# Caso 3: Contraseña Fuerte
p3 = "Correcto!__77CODEpy"
valida3, errores3 = validar_password(p3)
print(f"\nProbando: '{p3}'")
print(f"Válida: {valida3}")
print("Errores:", errores3)