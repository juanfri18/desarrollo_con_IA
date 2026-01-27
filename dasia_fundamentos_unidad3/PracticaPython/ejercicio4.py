import numpy as np

np.random.seed(123)
calificaciones = np.round(np.random.uniform(4, 10, size=(20, 5)), 1)
asignaturas = np.array(["Matemáticas", "Física", "Programación", "Inglés", "Historia"])

print(" APARTADO A ")
def estudiantes_aprobados(matriz_notas, nota_minima=5.0):
    # Compruebo si el estudiante aprobó TODAS las asignaturas 
    aprobo_todo = np.all(matriz_notas >= nota_minima, axis=1)
    
    # Obtengo los índices de quienes cumplen la condición
    indices = np.where(aprobo_todo)[0] 
    
    print(f"Estudiantes que aprobaron todo: {len(indices)}")
    return indices

indices_cracks = estudiantes_aprobados(calificaciones)
print(f"Índices de los aprobados: {indices_cracks}")

print("\n APARTADO B ")
# Calculo estadísticas por asignatura 
medias_asig = np.mean(calificaciones, axis=0)
print(f"Notas medias por asignatura: {medias_asig}")

# Busco la mejor asignatura
pos_mejor = np.argmax(medias_asig)
print(f"Mejor asignatura: {asignaturas[pos_mejor]} con {medias_asig[pos_mejor]:.2f}")

# Busco la peor asignatura
pos_peor = np.argmin(medias_asig)
print(f"Peor asignatura: {asignaturas[pos_peor]} con {medias_asig[pos_peor]:.2f}")

# Calculo la desviación estándar
desviaciones = np.std(calificaciones, axis=0)
pos_variable = np.argmax(desviaciones)
print(f"Asignatura más variable: {asignaturas[pos_variable]}")

print("\n APARTADO C ")
# Calculo la nota media de cada estudiante
medias_estudiantes = np.mean(calificaciones, axis=1)

# Defino las condiciones de clasificación
condiciones = [
    medias_estudiantes >= 9,
    (medias_estudiantes >= 7) & (medias_estudiantes < 9),
    (medias_estudiantes >= 6) & (medias_estudiantes < 7),
    (medias_estudiantes >= 5) & (medias_estudiantes < 6),
    medias_estudiantes < 5
]
etiquetas = ["Excelente", "Notable", "Bien", "Aprobado", "Suspenso"]

# Aplico la clasificación con np.select
clasificacion = np.select(condiciones, etiquetas)
print("Clasificación de los primeros 5 alumnos:")
print(clasificacion[:5])

print("\n--- APARTADO D (Avanzado) ---")
# 1. Busco el mejor estudiante en cada asignatura
mejores_indices = np.argmax(calificaciones, axis=0)
print(f"Índices de los mejores estudiantes por asig: {mejores_indices}")

# 2. Calculo la diferencia respecto a la media de la asignatura
diferencias = calificaciones - medias_asig

# 3. Filtro solo las diferencias positivas 
diferencias_positivas = np.where(diferencias > 0, diferencias, 0)

# Sumo las diferencias positivas por estudiante
suma_diferencias = np.sum(diferencias_positivas, axis=1)

# Encuentro al estudiante con mayor suma
indice_ganador = np.argmax(suma_diferencias)
print(f"Estudiante con mayor desviación positiva total: Índice {indice_ganador}")