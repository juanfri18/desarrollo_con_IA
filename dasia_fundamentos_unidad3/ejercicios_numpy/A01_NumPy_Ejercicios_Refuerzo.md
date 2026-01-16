# A02 - Ejercicios de refuerzo: NumPy

## Objetivo

Practicar y reforzar los conceptos fundamentales de numpy necesarios para trabajar con librerías de ciencia de datos e inteligencia artificial. Estos ejercicios **no son evaluables**, sino que están diseñados para consolidar tu aprendizaje mediante la práctica.

## Requisitos previos

- Haber completado la **U4 - NumPy: Arrays y Datos**
- Tener instalado NumPy (`pip install numpy`)
- Conocimientos básicos de Python (sintaxis, estructuras de control, funciones)


## Instrucciones generales

- Crea un archivo `.py` para cada ejercicio
- Prueba tu código con diferentes valores de entrada
- Si te atascas, revisa los apuntes de la U3.2


## Ejercicio 1: Creación y exploración de arrays (Nivel: ⭐)

**Contexto**: Familiarízate con la creación de arrays y sus propiedades básicas.

### Tareas:

**a)** Crea un array unidimensional con los números del 0 al 9 usando `np.arange()`.

**b)** Crea un array de 3x4 (3 filas, 4 columnas) lleno de ceros.

**c)** Crea un array de 2x5 lleno de unos.

**d)** Crea una matriz identidad de 4x4 (1 en la diagonal, 0 en el resto).

**e)** Para cada array creado, muestra:
   - Su forma (shape)
   - Su número de dimensiones
   - Su tamaño total (número de elementos)
   - Su tipo de dato

```python
import numpy as np

# a) Array del 0 al 9


# b) Array 3x4 de ceros


# c) Array 2x5 de unos


# d) Matriz identidad 4x4


# e) Explorar propiedades de cada array

```

**Resultado esperado**:
```
Array 0-9: [0 1 2 3 4 5 6 7 8 9]
Shape: (10,), Dimensiones: 1, Tamaño: 10, Tipo: int32
...
```

---

## Ejercicio 2: Indexación y slicing (Nivel: ⭐)

**Contexto**: Aprende a acceder y extraer elementos de arrays, similar a como se hace con arrays en Java pero con sintaxis más potente.

Dado el siguiente array:
```python
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
```

### Tareas:

**a)** Obtén el primer elemento del array.

**b)** Obtén el último elemento del array (usa índice negativo).

**c)** Obtén los elementos desde el índice 2 hasta el 5 (sin incluir el 5).

**d)** Obtén todos los elementos desde el índice 5 hasta el final.

**e)** Obtén todos los elementos desde el inicio hasta el índice 4 (sin incluir el 4).

**f)** Obtén todos los elementos en posiciones pares (índices 0, 2, 4, 6, ...).

**g)** Invierte el array completo usando slicing.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# a) Primer elemento


# b) Último elemento


# c) Elementos del índice 2 al 5


# d) Desde índice 5 hasta el final


# e) Desde el inicio hasta índice 4


# f) Elementos en posiciones pares


# g) Array invertido


```

**Comparación con Java**:
```java
// En Java harías:
int[] arr = {10, 20, 30, 40, 50};
int primero = arr[0];
int ultimo = arr[arr.length - 1];
// Para slicing necesitarías Arrays.copyOfRange() o bucles
```

---

## Ejercicio 3: Operaciones aritméticas básicas (Nivel: ⭐⭐)

**Contexto**: NumPy permite operaciones vectorizadas (aplicar operación a todos los elementos sin bucles).

### Tareas:

**a)** Crea dos arrays:
   - `a = [1, 2, 3, 4, 5]`
   - `b = [10, 20, 30, 40, 50]`

**b)** Realiza las siguientes operaciones **elemento a elemento**:
   - Suma: `a + b`
   - Resta: `b - a`
   - Multiplicación: `a * b`
   - División: `b / a`
   - Potencia: `a ** 2` (cada elemento al cuadrado)

**c)** Multiplica el array `a` por el escalar 10 (broadcasting).

**d)** Suma 100 a todos los elementos del array `b`.

**e)** Calcula la raíz cuadrada de cada elemento de `b` usando `np.sqrt()`.

```python
import numpy as np

# a) Crear arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# b) Operaciones elemento a elemento


# c) Multiplicar por escalar


# d) Sumar escalar


# e) Raíz cuadrada


```

**Comparación con Java**:
```java
// En Java necesitarías un bucle para cada operación:
for (int i = 0; i < a.length; i++) {
    suma[i] = a[i] + b[i];
}
// NumPy lo hace en UNA línea: suma = a + b
```

---

## Ejercicio 4: Arrays bidimensionales y operaciones por eje (Nivel: ⭐⭐)

**Contexto**: Trabaja con matrices (arrays 2D) y aprende a operar por filas o columnas.

Dada la siguiente matriz de ventas (3 tiendas, 4 trimestres):
```python
ventas = np.array([
    [1000, 1200, 1100, 1300],  # Tienda 1
    [900, 1000, 950, 1050],     # Tienda 2
    [1500, 1600, 1550, 1700]    # Tienda 3
])
```

### Tareas:

**a)** Muestra el shape de la matriz.

**b)** Obtén las ventas de la Tienda 2 (fila 1, índice 1).

**c)** Obtén las ventas del Trimestre 3 de todas las tiendas (columna 2).

**d)** Calcula el **total de ventas por tienda** (suma por filas, axis=1).

**e)** Calcula el **total de ventas por trimestre** (suma por columnas, axis=0).

**f)** Calcula las **ventas medias por tienda**.

**g)** Encuentra la **tienda con mayores ventas totales** (usa `np.argmax` sobre la suma por filas).

**h)** Encuentra el **trimestre con menores ventas totales** (usa `np.argmin` sobre la suma por columnas).

```python
import numpy as np

ventas = np.array([
    [1000, 1200, 1100, 1300],
    [900, 1000, 950, 1050],
    [1500, 1600, 1550, 1700]
])

# a) Shape


# b) Ventas Tienda 2


# c) Ventas Trimestre 3


# d) Total por tienda (suma por filas)


# e) Total por trimestre (suma por columnas)


# f) Media por tienda


# g) Tienda con mayores ventas


# h) Trimestre con menores ventas


```

**Concepto clave**: 
- `axis=0` → Opera por **columnas** (verticalmente)
- `axis=1` → Opera por **filas** (horizontalmente)

---

## Ejercicio 5: Máscaras booleanas y filtrado (Nivel: ⭐⭐)

**Contexto**: Las máscaras booleanas permiten filtrar datos según condiciones, similar a los streams con filter en Java.

Dado el siguiente array de temperaturas:
```python
temperaturas = np.array([18, 22, 25, 19, 30, 15, 28, 23, 17, 31, 20, 26])
```

### Tareas:

**a)** Crea una **máscara booleana** que identifique temperaturas mayores a 25°C.

**b)** Usa la máscara para obtener solo las temperaturas mayores a 25°C.

**c)** Cuenta cuántas temperaturas son mayores a 25°C (usa `np.sum` sobre la máscara).

**d)** Crea una máscara para temperaturas entre 20°C y 25°C (inclusive). Usa operadores lógicos `&` (AND).

**e)** Reemplaza todas las temperaturas mayores a 28°C por exactamente 28 (límite de seguridad).

**f)** Crea un nuevo array donde:
   - Temperaturas < 20 → "Frío"
   - Temperaturas entre 20-25 → "Templado"  
   - Temperaturas > 25 → "Calor"
   
   Pista: Usa `np.where()` anidado o `np.select()`.

```python
import numpy as np

temperaturas = np.array([18, 22, 25, 19, 30, 15, 28, 23, 17, 31, 20, 26])

# a) Máscara > 25


# b) Filtrar temperaturas > 25


# c) Contar temperaturas > 25


# d) Máscara entre 20 y 25


# e) Reemplazar valores > 28 con 28


# f) Clasificar temperaturas


```

**Comparación con Java**:
```java
// En Java usarías streams:
long count = Arrays.stream(temperaturas)
    .filter(t -> t > 25)
    .count();
// NumPy: np.sum(temperaturas > 25)
```

---

## Ejercicio 6: Estadísticas y análisis de datos (Nivel: ⭐⭐⭐)

**Contexto**: NumPy ofrece funciones estadísticas muy potentes para analizar datos.

Tienes las calificaciones de 5 estudiantes en 4 exámenes:
```python
calificaciones = np.array([
    [7.5, 8.0, 6.5, 9.0],   # Estudiante 1
    [5.0, 6.0, 5.5, 6.5],   # Estudiante 2
    [9.0, 9.5, 8.5, 10.0],  # Estudiante 3
    [6.0, 7.0, 6.5, 7.5],   # Estudiante 4
    [8.5, 8.0, 9.0, 8.5]    # Estudiante 5
])
```

### Tareas:

**a)** Calcula la **nota media de cada estudiante** (media por filas).

**b)** Calcula la **nota media de cada examen** (media por columnas).

**c)** Encuentra la **nota máxima y mínima de cada estudiante**.

**d)** Calcula la **desviación estándar de cada examen** (indica qué examen tuvo más variabilidad).

**e)** Identifica qué estudiantes tienen una **nota media ≥ 7.5** (aprobado con buena nota).

**f)** Encuentra el **estudiante con mejor nota media** (usa `np.argmax`).

**g)** Encuentra el **examen más difícil** (el que tiene la nota media más baja).

**h)** Crea una matriz que muestre la **diferencia de cada nota respecto a la media de su examen**.

```python
import numpy as np

calificaciones = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [5.0, 6.0, 5.5, 6.5],
    [9.0, 9.5, 8.5, 10.0],
    [6.0, 7.0, 6.5, 7.5],
    [8.5, 8.0, 9.0, 8.5]
])

# a) Nota media por estudiante


# b) Nota media por examen


# c) Máximo y mínimo por estudiante


# d) Desviación estándar por examen


# e) Estudiantes con media ≥ 7.5


# f) Mejor estudiante


# g) Examen más difícil


# h) Diferencias respecto a la media del examen


```

---

## Ejercicio 7: Reshape y manipulación de forma (Nivel: ⭐⭐⭐)

**Contexto**: Cambiar la forma de los arrays es fundamental para preparar datos para algoritmos de ML.

### Tareas:

**a)** Crea un array con los números del 1 al 12 usando `np.arange()`.

**b)** Reorganiza el array en una matriz de 3x4.

**c)** Reorganiza el array en una matriz de 4x3.

**d)** Reorganiza el array en una matriz de 2x6.

**e)** Usa `reshape(-1, 2)` para crear una matriz con 2 columnas (filas automáticas).

**f)** Transpón la matriz de 3x4 (intercambia filas por columnas).

**g)** Aplana la matriz de 3x4 a un array 1D usando `.flatten()`.

**h)** Crea una matriz 2x2x3 (array 3D) con los números del 1 al 12.

```python
import numpy as np

# a) Array 1-12


# b) Reshape a 3x4


# c) Reshape a 4x3


# d) Reshape a 2x6


# e) Reshape con -1 (automático)


# f) Transponer 3x4


# g) Aplanar (flatten)


# h) Array 3D (2x2x3)


```

**Nota importante**: 
- `reshape()` requiere que el número total de elementos coincida
- `-1` en reshape significa "calcula automáticamente esta dimensión"

---

## Ejercicio 8: Broadcasting (Nivel: ⭐⭐⭐)

**Contexto**: Broadcasting permite operar arrays de diferentes formas sin copiar datos explícitamente.

### Tareas:

**a)** Tienes una matriz de precios (3 productos, 4 meses):
```python
precios = np.array([
    [10, 12, 11, 13],   # Producto A
    [20, 22, 21, 23],   # Producto B
    [15, 17, 16, 18]    # Producto C
])
```
Aplica un descuento diferente a cada producto:
- Producto A: 10% descuento
- Producto B: 15% descuento
- Producto C: 5% descuento

Crea un array `descuentos = np.array([0.9, 0.85, 0.95])` y multiplícalo con `precios` usando broadcasting.

**b)** Normaliza cada fila de la matriz `precios` restando su media y dividiendo por su desviación estándar (normalización z-score por producto).

**c)** Crea una matriz 4x4 y súmale el array `[1, 2, 3, 4]` a cada fila (broadcasting).

**d)** Crea una matriz 3x5 de números aleatorios entre 0 y 1. Súmale un array columna `[[10], [20], [30]]` (broadcasting vertical).

```python
import numpy as np

# a) Aplicar descuentos diferentes a cada producto
precios = np.array([
    [10, 12, 11, 13],
    [20, 22, 21, 23],
    [15, 17, 16, 18]
])
descuentos = np.array([0.9, 0.85, 0.95])

# Broadcasting requiere shape compatible


# b) Normalización z-score por fila


# c) Broadcasting suma por fila


# d) Broadcasting suma por columna


```

**Concepto clave**: Broadcasting funciona cuando:
- Las dimensiones son iguales, O
- Una de las dimensiones es 1, O
- Una dimensión no existe (se expande automáticamente)

---

## Ejercicio 9: Análisis de datos reales - Simulación de sensores (Nivel: ⭐⭐⭐⭐)

**Contexto**: Simula datos de 10 sensores de temperatura tomando mediciones cada hora durante un día (24 horas).

### Tareas:

**a)** Crea una matriz 10x24 con datos aleatorios de temperatura entre 15°C y 35°C (usa `np.random.uniform()`).

**b)** Calcula la **temperatura media, máxima y mínima** de cada sensor durante el día.

**c)** Calcula la **temperatura media por hora** (promedio de todos los sensores en cada hora).

**d)** Identifica las **horas críticas** donde la temperatura media supera los 30°C.

**e)** Encuentra el **sensor más estable** (el que tiene menor desviación estándar).

**f)** Encuentra el **sensor más variable** (el que tiene mayor desviación estándar).

**g)** Crea una **matriz de alertas** (booleana) que marque `True` donde la temperatura supera los 32°C.

**h)** Cuenta cuántas alertas tiene cada sensor (suma por filas de la matriz booleana).

**i)** Normaliza los datos de cada sensor entre 0 y 1 usando Min-Max scaling:
   ```
   temperatura_norm = (temperatura - min_sensor) / (max_sensor - min_sensor)
   ```

**j)** Calcula la **diferencia entre la temperatura máxima y mínima de cada hora** (rango horario).

```python
import numpy as np

np.random.seed(42)  # Para reproducibilidad

# a) Crear datos de sensores (10 sensores, 24 horas)


# b) Estadísticas por sensor


# c) Temperatura media por hora


# d) Horas críticas (>30°C)


# e) Sensor más estable


# f) Sensor más variable


# g) Matriz de alertas


# h) Alertas por sensor


# i) Normalización Min-Max por sensor


# j) Rango horario (max-min por hora)


```

**Resultado esperado**:
```
Sensor más estable: Sensor 3 (σ=2.45)
Sensor más variable: Sensor 7 (σ=5.21)
Horas críticas: [12, 13, 14, 15, 16]
...
```

---

## Ejercicio 10: Desafío final - Sistema de recomendación simple (Nivel: ⭐⭐⭐⭐⭐)

**Contexto**: Crea un sistema básico de recomendación usando similitud de coseno entre usuarios.

Tienes una matriz de valoraciones de películas (5 usuarios, 6 películas):
- Valores de 1-5 (estrellas), 0 = no vista

```python
valoraciones = np.array([
    [5, 3, 0, 1, 4, 2],   # Usuario 1
    [4, 0, 0, 1, 3, 5],   # Usuario 2
    [1, 1, 0, 5, 0, 3],   # Usuario 3
    [0, 0, 5, 4, 0, 0],   # Usuario 4
    [5, 4, 4, 0, 3, 0]    # Usuario 5
])
```

### Tareas:

**a)** Calcula la **media de valoración de cada usuario** (ignorando películas no vistas, valor 0).
   - Pista: Usa máscaras booleanas o `np.ma.masked_equal()`.

**b)** Normaliza las valoraciones restando la media de cada usuario (solo a las películas vistas).

**c)** Calcula la **similitud de coseno** entre el Usuario 1 y todos los demás usuarios:
   ```
   similitud = (A · B) / (||A|| * ||B||)
   ```
   - Pista: Usa `np.dot()` para el producto punto y `np.linalg.norm()` para la norma.

**d)** Encuentra el **usuario más similar al Usuario 1** (excluyendo al propio Usuario 1).

**e)** Recomienda películas al Usuario 1:
   - Encuentra películas que el Usuario 1 NO ha visto (valor 0)
   - De esas, recomienda las que el usuario más similar SÍ ha visto y valoró bien (≥4)

**f)** Calcula la **película más popular** (la que tiene más valoraciones ≥4).

**g)** Identifica **usuarios con gustos similares** (similitud de coseno ≥ 0.7).

```python
import numpy as np

valoraciones = np.array([
    [5, 3, 0, 1, 4, 2],
    [4, 0, 0, 1, 3, 5],
    [1, 1, 0, 5, 0, 3],
    [0, 0, 5, 4, 0, 0],
    [5, 4, 4, 0, 3, 0]
])

peliculas = ["Matrix", "Titanic", "Avatar", "Inception", "Interstellar", "Star Wars"]

# a) Media por usuario (ignorando 0s)
def media_usuario(valoraciones_usuario):
    # Solo promediar valores > 0
    pass


# b) Normalizar valoraciones


# c) Similitud de coseno Usuario 1 vs resto
def similitud_coseno(usuario1, usuario2):
    # Calcular similitud solo con películas vistas por ambos
    pass


# d) Usuario más similar al Usuario 1


# e) Recomendar películas al Usuario 1


# f) Película más popular


# g) Pares de usuarios similares


```

**Resultado esperado**:
```
Usuario más similar a Usuario 1: Usuario 5 (similitud: 0.85)
Películas recomendadas para Usuario 1: ['Avatar', 'Interstellar']
Película más popular: Inception (4 valoraciones ≥4)
```

---

## Soluciones y auto-evaluación

### ¿Cómo saber si lo has hecho bien?

Para cada ejercicio:

1. **El código se ejecuta sin errores** ✅
2. **Los resultados tienen sentido lógicamente** ✅
3. **Usas funciones de NumPy** (no bucles manuales) ✅
4. **El código es legible** (nombres descriptivos, comentarios) ✅

### Señales de que necesitas repasar:

- ❌ Usas bucles `for` donde NumPy tiene funciones vectorizadas
- ❌ No entiendes qué es `axis=0` vs `axis=1`
- ❌ No sabes usar máscaras booleanas para filtrar
- ❌ Te confundes con el broadcasting
- ❌ No sabes cuándo usar `reshape` vs `flatten` vs `ravel`

### Recursos adicionales:

- **Documentación oficial**: https://numpy.org/doc/stable/
- **NumPy para programadores Java**: https://numpy.org/doc/stable/user/numpy-for-matlab-users.html
- **Cheat sheet**: https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf
