# Datos de entrada
usuarios_intereses = {
    "Ana": {"Python", "Machine Learning", "Data Science", "Música"},
    "Carlos": {"JavaScript", "React", "Node.js", "Videojuegos"},
    "Elena": {"Python", "Data Science", "Estadística", "Lectura"},
    "David": {"Python", "Django", "PostgreSQL", "Música"},
    "Lucia": {"Música", "Videojuegos", "Caminar"}
}

def encontrar_usuarios_similares(usuario, minimo_coincidencias=2):
    """
    Devuelve una lista de nombres de usuarios que tienen al menos 
    'minimo_coincidencias' intereses en común con el usuario dado.
    """
    if usuario not in usuarios_intereses:
        return []

    intereses_usuario = usuarios_intereses[usuario]
    usuarios_similares = []

    for otro_usuario, otros_intereses in usuarios_intereses.items():
        # No comparamos al usuario consigo mismo
        if otro_usuario == usuario:
            continue
        
        # Calculamos la intersección (elementos comunes)
        coincidencias = intereses_usuario.intersection(otros_intereses)
        
        if len(coincidencias) >= minimo_coincidencias:
            usuarios_similares.append(otro_usuario)
            
    return usuarios_similares

def recomendar_intereses(usuario):
    """
    Busca usuarios similares y devuelve una lista de intereses que esos
    usuarios tienen pero que el usuario original no tiene.
    """
    if usuario not in usuarios_intereses:
        return "Usuario no encontrado"

    intereses_propios = usuarios_intereses[usuario]
    usuarios_similares = encontrar_usuarios_similares(usuario)
    
    # Usamos un conjunto para evitar recomendaciones duplicadas automáticamente
    recomendaciones = set()

    for sim_user in usuarios_similares:
        intereses_ajenos = usuarios_intereses[sim_user]
        
        # Operación de diferencia: Lo que tiene el otro MENOS lo que tengo yo
        # intereses_ajenos - intereses_propios
        nuevos_temas = intereses_ajenos.difference(intereses_propios)
        
        # Añadimos los nuevos temas al conjunto de recomendaciones
        recomendaciones.update(nuevos_temas)

    return list(recomendaciones)

# --- PRUEBAS ---
print(f"Intereses de Ana: {usuarios_intereses['Ana']}")
print("---")
print(f"Usuarios similares a Ana: {encontrar_usuarios_similares('Ana')}")
print(f"Recomendaciones para Ana: {recomendar_intereses('Ana')}")