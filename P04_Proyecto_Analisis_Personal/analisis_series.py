import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. CARGA DE DATOS
# ==========================================
print("--- CARGANDO DATOS ---")
# Usamos read_csv como indica la teoría U4.2
df = pd.read_csv('dataset_series.csv')

# Vemos las primeras filas y la información general
print(df.head())
print("\nInformación del DataFrame:")
df.info()

# ==========================================
# 2. LIMPIEZA DE DATOS (Requisito U4.1 y U4.3)
# ==========================================
print("\n--- LIMPIEZA DE DATOS ---")

# Verificar nulos
nulos = df.isnull().sum()
print(f"Valores nulos por columna:\n{nulos}")

# Verificar duplicados
duplicados = df.duplicated().sum()
print(f"Filas duplicadas: {duplicados}")

# Si hubiera nulos, los eliminaríamos (teoría U4.3)
# df = df.dropna() 

# ==========================================
# 3. ANÁLISIS ESTADÍSTICO (Requisito U4.3)
# ==========================================
print("\n--- ESTADÍSTICAS ---")

# Estadística descriptiva general
print(df.describe())

# Cálculo específico 1: Media de puntuación
media_puntos = df['puntuacion'].mean()
print(f"\nMi puntuación media es: {media_puntos:.2f}")

# Cálculo específico 2: Serie más larga (más temporadas)
max_temporadas = df.sort_values('temporadas', ascending=False).iloc[0]
print(f"Serie más larga: {max_temporadas['titulo']} ({max_temporadas['temporadas']} temporadas)")

# Agrupación 1: Puntuación media por Género (GroupBy - U4.3)
print("\nPuntuación media por género:")
print(df.groupby('genero')['puntuacion'].mean().sort_values(ascending=False))

# Agrupación 2: Cuántas series veo por Plataforma (Value Counts - U4.3)
print("\nSeries por plataforma:")
conteo_plataforma = df['plataforma'].value_counts()
print(conteo_plataforma)

# ==========================================
# 4. VISUALIZACIONES (Requisito P04)
# ==========================================
# Gráfico 1: Barras - Series por Plataforma
plt.figure(figsize=(10, 6))
conteo_plataforma.plot(kind='bar', color='skyblue')
plt.title('Número de series vistas por Plataforma')
plt.xlabel('Plataforma')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_barras_plataformas.png') # Guardar imagen
plt.show()

# Gráfico 2: Histograma - Distribución de Puntuaciones
plt.figure(figsize=(10, 6))
df['puntuacion'].plot(kind='hist', bins=10, color='orange', edgecolor='black')
plt.title('Distribución de mis puntuaciones')
plt.xlabel('Puntuación')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.savefig('grafico_hist_puntuacion.png')
plt.show()

# Gráfico 3: Dispersión - Año vs Puntuación
plt.figure(figsize=(10, 6))
plt.scatter(df['anio_inicio'], df['puntuacion'], color='purple')
plt.title('Relación: Año de estreno vs Puntuación')
plt.xlabel('Año de Estreno')
plt.ylabel('Puntuación')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('grafico_scatter_anio.png')
plt.show()

print("\n✅ ¡Análisis completado y gráficos guardados!")