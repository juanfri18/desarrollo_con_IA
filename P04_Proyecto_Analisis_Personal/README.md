# Proyecto de Análisis de Series (P04)

**Autor:** Juan F.
**Curso:** Desarrollo con IA
**Fecha:** Febrero 2024

## 📋 Descripción
Este proyecto consiste en un análisis de datos personal sobre mis hábitos de consumo de series de televisión. El objetivo es aplicar las técnicas aprendidas de **Pandas** y **Matplotlib** para extraer conclusiones sobre mis géneros favoritos, plataformas más usadas y patrones de puntuación.

## 📂 Estructura del proyecto
- `analisis_series.py`: Script principal de Python que realiza la carga, limpieza y análisis.
- `dataset_series.csv`: Archivo de datos con 20 registros de series.
- `requirements.txt`: Lista de librerías necesarias.
- `graficos/*.png`: Visualizaciones generadas automáticamente.

## 🛠️ Tecnologías utilizadas
- **Python 3.14**
- **Pandas**: Para la manipulación del DataFrame (filtrado, agrupación y cálculo de medias).
- **Matplotlib**: Para la generación de gráficos de barras, histogramas y dispersión.

## 📊 Hallazgos principales
1. **Plataformas**: Netflix es la plataforma predominante en mi historial de visualización.
2. **Puntuaciones**: Mis valoraciones tienden a concentrarse entre el 8.0 y el 9.0, indicando que suelo ser selectivo con lo que veo.
3. **Tendencias**: Las series de drama y ciencia ficción ocupan la mayor parte de mi tiempo de visualización.

## 🚀 Cómo ejecutar
1. Instalar las dependencias:
```bash
   pip install -r requirements.txt

```

2. Ejecutar el script de análisis:
```bash
python analisis_series.py

```



```

---

### 2. Guía para tu Presentación (PowerPoint / PDF)

Abre PowerPoint (o Google Slides) y crea una presentación de **8 diapositivas**. Copia y pega estos textos:

* **Diapositiva 1: Portada**
    * **Título grande:** Análisis de Datos: Mis Series de TV
    * **Subtítulo:** Práctica P04 - Fundamentos de Pandas
    * **Nombre:** Juan F.

* **Diapositiva 2: Introducción**
    * **Objetivo:** Analizar mi historial de visualización de series para descubrir patrones de consumo.
    * **Herramientas:** Python, Pandas y Matplotlib.
    * **Dataset:** Creado manualmente con 20 registros reales de series que he visto (Breaking Bad, Stranger Things, etc.).

* **Diapositiva 3: El Código (Carga y Limpieza)**
    * *Texto:* "Utilicé Pandas para cargar el CSV y verificar la calidad de los datos."
    * *Pon una captura de pantalla de estas líneas de tu código:*
        ```python
        df = pd.read_csv('dataset_series.csv')
        nulos = df.isnull().sum()
        duplicados = df.duplicated().sum()
        ```

* **Diapositiva 4: Análisis Estadístico**
    * *Texto:* "Gracias a la función `describe()` y `groupby()` obtuve estos datos:"
    * *Puntos clave:*
        * Serie más larga: Lost (121 capítulos vistos).
        * Puntuación media global: 8.7
        * Género mejor valorado: Drama.

* **Diapositiva 5: Visualización 1 - Plataformas**
    * *Título:* ¿Dónde veo mis series?
    * **[IMPORTANTE]**: Pega aquí la imagen `grafico_barras_plataformas.png` que generó tu código.
    * *Comentario:* "Se observa una clara preferencia por las plataformas de streaming principales."

* **Diapositiva 6: Visualización 2 - Puntuaciones**
    * *Título:* Distribución de mis notas
    * **[IMPORTANTE]**: Pega aquí la imagen `grafico_hist_puntuacion.png`.
    * *Comentario:* "La mayoría de series reciben una nota alta (entre 8 y 9.5), lo que sugiere que suelo terminar solo las series que me gustan mucho."

* **Diapositiva 7: Visualización 3 - Tendencia Temporal**
    * *Título:* Año de estreno vs Calidad
    * **[IMPORTANTE]**: Pega aquí la imagen `grafico_scatter_anio.png`.
    * *Comentario:* "No existe una correlación fuerte entre la antigüedad de la serie y la nota que le pongo."

* **Diapositiva 8: Conclusiones**
    * Pandas facilita enormemente el procesamiento de datos estructurados.
    * La limpieza de datos inicial fue clave para evitar errores (nulos/duplicados).
    * Visualmente es más fácil entender mis hábitos que mirando la tabla de Excel.

---

