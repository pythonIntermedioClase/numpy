# Sesión 4: NumPy

**Python Intermedio para Análisis de Datos — DIAN 2026**

## ¿Qué hay en este repositorio?

Ejercicios de la Sesión 4. Practicamos operaciones con arrays de NumPy aplicadas
a datos tributarios simulados: vectorización, slicing, máscaras booleanas y
lógica condicional con `np.where`.

```
repositorio_plantilla_sesion_04/
├── main.py              ← Punto de entrada. Ejecuta el menú interactivo.
├── requirements.txt     ← Dependencias del proyecto (numpy).
├── src/
│   ├── __init__.py
│   └── numpy_utils.py   ← Funciones NumPy del proyecto.
└── data/
    ├── input/           ← Archivos de entrada. Vacío por ahora.
    └── output/          ← Resultados generados.
```

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Flujo de trabajo

1. Implementa cada función en `src/numpy_utils.py`.
2. Descomenta el bloque correspondiente en `main.py`.
3. Ejecuta `python main.py` y verifica la salida.
4. `git add`, `commit` y `push` al terminar cada sección.


**Curso:** Python Intermedio para Análisis de Datos — DIAN 2026  
**Duración:** 4 horas (240 min) 
---

## Índice

- [Sección 0 — Configurar el nuevo entorno](#sección-0--configurar-el-nuevo-entorno)
- [De dónde viene NumPy](#de-dónde-viene-numpy)
- [Sección 1 — Arrays y tipos de datos](#sección-1--arrays-y-tipos-de-datos)
- [Sección 2 — Indexación y slicing](#sección-2--indexación-y-slicing)
- [Pausa](#pausa)
- [Sección 3 — Vectorización](#sección-3--vectorización)
- [Sección 4 — Funciones universales (ufuncs)](#sección-4--funciones-universales-ufuncs)
- [Sección 5 — Arrays booleanos](#sección-5--arrays-booleanos)
- [Sección 6 — np.where](#sección-6--npwhere)
- [Cierre](#cierre)
- [Aparte — Python y el análisis de datos](#aparte--python-y-el-análisis-de-datos)

---

## Sección 0 — Configurar el nuevo entorno

### 0.1 Aceptar la tarea en GitHub Classroom

1. Se compartirá un enlace de GitHub Classroom en el chat.
2. Haz clic en el enlace e inicia sesión con tu cuenta de GitHub.
3. Acepta la tarea. GitHub creará automáticamente un repositorio personal con el código de esta sesión.
4. Copia la URL de tu repositorio (botón verde **Code → HTTPS**).

### 0.2 Abrir un nuevo Codespace

Cada repositorio necesita su propio Codespace. El Codespace de la sesión 2-3 sigue disponible para consultar código anterior, pero el trabajo de hoy ocurre en este repositorio.

1. En tu repositorio de sesión 4, haz clic en **Code → Codespaces → Create codespace on main**.
2. Espera a que cargue el entorno (1-2 min la primera vez).
3. Cuando veas el editor con la terminal integrada, estás listo.

### 0.3 Revisar la estructura del proyecto
``

> **¿Para qué sirve cada parte?**
> - `src/numpy_utils.py`, las funciones que vas a implementar hoy.
> - `data/input/`, archivos de entrada (CSVs, Excel). Vacía por ahora.
> - `data/output/`, resultados exportados por el programa. Vacía por ahora.
> - `requirements.txt`, lista de librerías externas necesarias.

### 0.4 Crear el entorno virtual e instalar dependencias

A diferencia de las sesiones 1-3 donde Python y su librería estándar son suficientes, esta sesión usa **NumPy**, una librería externa. Cada proyecto tiene su propio entorno virtual para aislar sus dependencias.

```bash
# Crear el entorno virtual
python -m venv .venv

# Activarlo (Linux / macOS / Codespaces)
source .venv/bin/activate
```

Cuando está activo, el prompt de la terminal cambia a:

```
(.venv) $
```

Instala las dependencias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

Verás algo como:

```
Collecting numpy
  Downloading numpy-2.x.x-...whl (...)
Successfully installed numpy-2.x.x
```

### 0.5 Verificar la instalación

```bash
python -c "import numpy as np; print('NumPy', np.__version__, '— OK')"
```

Salida esperada:

```
NumPy 2.x.x — OK
```

### 0.6 Primer commit

Antes de escribir código, registra el punto de partida:

```bash
git add .
git commit -m "sesion-04: inicio — entorno configurado"
git push
```

### 0.6 Instalar las extensiones de Python

Codespaces a veces instala extensiones recomendadas de forma automática, pero conviene confirmarlo antes de seguir.

1. Abre el panel de extensiones con el ícono de bloques en la barra lateral izquierda (o `Ctrl+Shift+X` en Windows/Linux, `Cmd+Shift+X` en Mac).
2. Busca **Python**, la extensión publicada por Microsoft, y haz clic en **Install** si todavía no aparece instalada.

> **¿Por qué importa esto?** Sin estas extensiones, el editor trata el código Python como texto plano: no resalta errores de sintaxis, no sugiere autocompletado y no detecta a qué entorno virtual está apuntando.
---

## De dónde viene NumPy

> *"NumPy es la base sobre la que se construyó todo el ecosistema científico de Python."*  
> — Harris et al., *Nature*, 2020

### El problema original

Python nació en 1991 como un lenguaje de propósito general: fácil de leer, fácil de aprender, ideal para automatizar tareas y escribir scripts. Pero tenía una limitación importante cuando se trataba de cálculos numéricos: era lento.

A mediados de los años 90, los científicos que querían usar Python para análisis estadístico, simulaciones o procesamiento de datos se encontraban con el mismo obstáculo: las listas de Python, aunque flexibles, no estaban diseñadas para matemáticas de alto rendimiento. Calcular el promedio de un millón de mediciones era órdenes de magnitud más lento que hacerlo en Fortran o C.

### Dos librerías, un problema

La comunidad respondió con dos proyectos independientes:

| Librería | Año | Origen |
|---|---|---|
| **Numeric** | 1995 | Paul Dubois y Jim Hugunin, primeros arrays para Python |
| **Numarray** | 2001 | Space Telescope Science Institute (NASA/STScI), mejor soporte para arrays grandes |

El problema: las dos eran incompatibles entre sí. Un código escrito con `Numeric` no funcionaba con `Numarray`. Los proyectos se fragmentaron y la comunidad tuvo que elegir uno u otro.

### Travis Oliphant unifica todo

En 2005, **Travis Oliphant**, matemático e ingeniero, tomó las mejores ideas de ambas librerías y las fusionó en un solo proyecto. El resultado fue **NumPy 1.0**, lanzado en **2006**.

El nombre es directo: **Num**erical **Py**thon, Python numérico.

La apuesta era clara: si la comunidad científica tenía *una* librería de arrays en común, todo lo demás podría construirse encima. Y así fue.

### El efecto en cascada

Desde 2006, NumPy se convirtió en la capa base de casi todo el ecosistema de análisis de datos en Python:

```
NumPy  →  pandas, SciPy, matplotlib, scikit-learn, TensorFlow, PyTorch...
```

Cuando cargas un DataFrame en pandas, cuando entrenas un modelo, cuando graficas una distribución, todo eso usa arrays de NumPy por debajo, aunque no lo veas directamente.

### El reconocimiento académico

En septiembre de **2020**, la revista *Nature* publicó el artículo *"Array programming with NumPy"*, firmado por más de 30 autores de universidades, laboratorios y empresas tecnológicas de todo el mundo.

Que una librería de software reciba un artículo en *Nature* no es frecuente. Es el reconocimiento de que NumPy es una pieza de infraestructura científica global, no solo una herramienta de programación.

> Harris, C. R., et al. (2020). *Array programming with NumPy*. Nature, 585, 357–362.  
> [doi.org/10.1038/s41586-020-2649-2](https://doi.org/10.1038/s41586-020-2649-2)

### Por qué importa en tu trabajo

Los modelos de lenguaje con los que interactúas hoy, GPT, Claude, Gemini, fueron entrenados sobre miles de millones de parámetros almacenados y actualizados en arrays NumPy. Los sistemas de detección de fraude financiero que procesan millones de transacciones en tiempo real usan las mismas máscaras booleanas que verás en la sección 5. Los modelos climáticos que proyectan temperaturas para 2050 corren sobre operaciones vectorizadas sobre grillas de cientos de millones de puntos.

La diferencia es de escala: una herramienta para procesar un elemento a la vez, otra para procesar millones.

---
## Sección 1 — Arrays y tipos de datos

### Antes de empezar: repaso rápido de listas
En la sesión 3 no llegamos a cubrir listas a fondo, así que antes de meternos con arrays, repasemos lo que vas a necesitar para seguir el resto de la sesión.

**Qué es una lista, en la práctica**

Una lista se crea con corchetes y guarda una secuencia ordenada de elementos:

```python
valores = [1_500_000, 850_000, 2_300_000]
```

Tres características la definen:

- **Es ordenada.** Cada elemento ocupa una posición fija hasta que algo la cambie. `valores[0]` siempre va a ser el primer elemento que agregaste, en ese orden.
- **Es mutable.** Puedes agregar, quitar o reemplazar elementos después de creada la lista, sin construir una lista nueva desde cero.
- **Acepta tipos mezclados.** Una misma lista puede contener números, texto y booleanos a la vez: `[1, "hola", True]` es válido para Python. En la práctica casi siempre vas a trabajar con listas de un solo tipo, pero vale la pena saber que la mezcla no produce un error.

**Funciones y métodos que vas a usar todo el tiempo como científico de datos**

| Operación | Sintaxis | Qué hace |
|---|---|---|
| Tamaño | `len(valores)` | Cuenta cuántos elementos tiene la lista |
| Agregar al final | `valores.append(x)` | Agrega `x` como último elemento |
| Insertar en una posición | `valores.insert(i, x)` | Agrega `x` en la posición `i`, desplazando el resto un lugar |
| Quitar por valor | `valores.remove(x)` | Elimina la primera aparición de `x` |
| Quitar por posición | `valores.pop(i)` | Elimina el elemento en la posición `i` y lo retorna |
| Ordenar | `valores.sort()` / `sorted(valores)` | `.sort()` ordena la lista original y no retorna nada útil; `sorted()` retorna una lista nueva y deja la original intacta |
| Contar apariciones | `valores.count(x)` | Cuenta cuántas veces aparece `x` en la lista |
| Encontrar una posición | `valores.index(x)` | Retorna la posición de la primera aparición de `x` |
| Suma, mínimo, máximo | `sum(valores)`, `min(valores)`, `max(valores)` | Funciones integradas de Python, no métodos de la lista |

```python
valores = [1_500_000, 850_000, 2_300_000]
valores.append(950_000)
print(valores)          # [1500000, 850000, 2300000, 950000]

total = sum(valores)
print(total)             # 5600000

valores.sort()
print(valores)           # [850000, 950000, 1500000, 2300000]
```

La distinción entre `.sort()` y `sorted()` . `.sort()` modifica la lista original "en el lugar" y la otra no toca nada y te entrega una copia ordenada.

**Indexar y recortar (slicing)**

Cada elemento tiene una posición, contada desde 0. Para acceder a un elemento puntual usas `lista[posición]`:

```python
valores = [1_500_000, 850_000, 2_300_000]

print(valores[0])    # 1500000, el primer elemento
print(valores[-1])   # 2300000, el último elemento (índice negativo: cuenta desde el final)
print(valores[-2])   # 850000, el penúltimo elemento
```

Para tomar un pedazo de la lista usas slicing: dos posiciones separadas por dos puntos, donde la primera es inclusiva y la segunda es exclusiva.

```python
print(valores[0:2])  # [1500000, 850000], posiciones 0 y 1
print(valores[1:])   # [850000, 2300000], desde la posición 1 hasta el final
print(valores[:2])   # [1500000, 850000], desde el inicio hasta antes de la posición 2
```

El slicing acepta un tercer número opcional, el paso:

```python
print(valores[::2])   # [1500000, 2300000], un elemento sí y uno no
print(valores[::-1])  # [2300000, 850000, 1500000], la lista invertida
```

**Recorrer una lista: dos formas**

La forma más directa recorre los elementos mismos:

```python
for valor in valores:
    print(valor)
# 1500000
# 850000
# 2300000
```

En cada vuelta del ciclo, `valor` toma el contenido de una posición distinta. No tienes acceso directo a en qué posición estás parado, solo al contenido.

La otra forma recorre las posiciones, usando `range(len(...))`:

```python
for i in range(len(valores)):
    print(i, valores[i])
# 0 1500000
# 1 850000
# 2 2300000
```

Aquí `i` es un número entero que avanza de 0 hasta `len(valores) - 1`. `valores[i]` te da el elemento en esa posición. Esta forma es más larga de escribir, pero se vuelve necesaria cuando el índice importa por sí mismo: por ejemplo, si necesitas comparar cada elemento con el siguiente, o si vas a modificar la lista original en esa misma posición (`valores[i] = valores[i] * 1.19`), algo que el primer ciclo no permite hacer directamente.

Hay un punto medio entre las dos formas: `enumerate()` te entrega la posición y el valor al mismo tiempo, sin que tengas que escribir `valores[i]` para conseguir el valor.

```python
for i, valor in enumerate(valores):
    print(i, valor)
# 0 1500000
# 1 850000
# 2 2300000
```

En la práctica: si solo necesitas el valor, usa `for valor in valores`. Si necesitas la posición y el valor juntos, usa `enumerate()`. Reserva `range(len(...))` para los casos en los que de verdad vas a modificar la lista original por posición.

Los arrays de NumPy retoman exactamente esta misma notación de índices, slices y recorridos, solo que con otras capacidades por debajo.

### ¿Por qué NumPy?

En las sesiones anteriores usamos listas de Python para guardar valores declarados:

```python
valores = [1_500_000, 850_000, 0, 2_300_000]
```

Para calcular el IVA de cada valor necesitábamos un ciclo `for` que procesaba los elementos uno por uno:

```python
iva = []
for valor in valores:
    iva.append(valor * 0.19)
# resultado: [285000.0, 161500.0, 0.0, 437000.0]
```

Esto funciona, pero tiene dos problemas: para cada cálculo hay que escribir un ciclo completo, y Python procesa un elemento a la vez. Con cientos de miles de declaraciones, eso se acumula en segundos o minutos de espera.

NumPy resuelve los dos problemas de golpe. La idea central se llama **vectorización**.

> **¿Qué significa "vectorizar" una operación?**  
> Vectorizar significa expresar una operación que aplica a *un* elemento de forma que se aplique automáticamente a *todos* los elementos de un conjunto, sin que escribas un ciclo. La operación se convierte en una instrucción única que el procesador puede ejecutar en lote.
>
> En la práctica: en lugar de escribir "para cada valor, multiplícalo por 0.19", escribes simplemente `valores * 0.19` y NumPy se encarga del resto. El ciclo sigue existiendo por dentro, pero ocurre en código C pre-compilado que corre a la velocidad del procesador, no en Python interpretado.
>
> Piénsalo así: si tienes 100 formularios para firmar, el ciclo `for` es firmar uno, volver a tu escritorio, tomar el siguiente, firmarlo, volver… La vectorización es estampar un sello que marca los 100 de una sola pasada.

### El tipo ndarray

La estructura principal de NumPy se llama **ndarray** (n-dimensional array, arreglo de n dimensiones). Para entender qué la diferencia de una lista, compara estas características:

| Característica | Lista Python | ndarray NumPy |
|---|---|---|
| Tipos mezclados | Sí: `[1, "hola", True]` es válido | No: todos los elementos deben ser del mismo tipo |
| Operaciones vectorizadas | No: requiere ciclo `for` | Sí: `arr * 0.19` opera sobre todos a la vez |
| Cómo guarda los datos en memoria | Referencias dispersas (como fichas con la dirección de cada valor) | Valores contiguos (uno al lado del otro, como celdas de una hoja de cálculo) |
| Velocidad en cálculo numérico | Lenta: Python itera uno a uno | Rápida: delega a funciones C compiladas |

Esa restricción de tipo único es lo que habilita la velocidad. Al saber de antemano que todos los elementos son, por ejemplo, `float64`, NumPy aplica la misma instrucción a todos sin detenerse a verificar el tipo de cada uno.

### Tipos de dato (dtype)

En Python, cuando escribes `x = 1_500_000`, Python decide automáticamente que `x` es un entero. Con NumPy tienes que ser explícito sobre el tipo porque ese tipo determina cuánta memoria ocupa cada elemento y qué operaciones se pueden hacer.

Los tipos más usados en análisis de datos son:

| dtype | Descripción | ¿Por qué usarlo? |
|---|---|---|
| `np.float64` | Número decimal de 64 bits de precisión | Valores declarados, tasas, cualquier cosa que pueda tener centavos |
| `np.int32` | Número entero de 32 bits | Días de mora, conteos, sin decimales |
| `np.bool_` | Verdadero o falso | Máscaras de filtrado (lo verás en la sección 5) |

> **¿Qué significa "64 bits"?**  
> Un bit es la unidad mínima de información en un computador: un 0 o un 1. Con 64 bits, un número puede representar hasta 2⁶⁴ combinaciones distintas, lo que permite guardar valores con hasta 15-16 dígitos significativos de precisión. Para montos en pesos colombianos eso es más que suficiente. Con 32 bits (`float32`) solo tienes 7 dígitos, lo que generaría errores de redondeo en valores grandes.

Veamos los tipos en acción:

```python
import numpy as np

# float64: los valores se muestran con punto decimal
valores = np.array([1_500_000, 850_000, 0, 2_300_000], dtype=np.float64)
print(valores)        # [1500000.   850000.        0.  2300000.]
print(valores.dtype)  # float64

# int32: sin punto decimal, solo enteros
dias = np.array([0, 30, 0, 45], dtype=np.int32)
print(dias)           # [ 0 30  0 45]
print(dias.dtype)     # int32

# shape: la "forma" del array, cuántos elementos hay en cada dimensión
print(valores.shape)  # (4,)
```

> **¿Qué es una tupla y por qué `shape` la usa?**  
>
> Una **tupla** es una secuencia de valores entre paréntesis: `(4,)`, `(100, 8)`, `(3, 4, 5)`. Se parece a una lista pero con dos diferencias importantes:
>
> 1. Se escribe con paréntesis `()` en lugar de corchetes `[]`.
> 2. Es **inmutable**: una vez creada, no se puede modificar. No tiene `.append()` ni `.remove()`.
>
> NumPy usa tuplas para describir la forma (`shape`) de un array porque la forma no debería cambiar accidentalmente. `(4,)` significa "un array de una sola dimensión con 4 elementos". La coma al final no es un error, es necesaria para distinguir una tupla de un solo elemento `(4,)` de una expresión matemática `(4)`.
>
> ¿Por qué varias dimensiones? Porque los datos reales tienen estructura. Un array plano de 8 valores declarados tiene `shape = (8,)`. Una tabla con 100 declaraciones y 8 columnas de atributos tendría `shape = (100, 8)`, eso son las matrices que usarás cuando llegues a pandas. Por ahora solo trabajamos con una dimensión.

### Punto de fallo — tipos mezclados en un array

```python
# ¿Qué pasa si mezclas números y texto?
mezclado = np.array([1_500_000, "sin datos", 2_300_000])
print(mezclado)
# ['1500000' 'sin datos' '2300000']  ← NumPy convierte TODO a string
print(mezclado.dtype)
# <U9   ← Unicode de 9 caracteres

# Intentar una operación numérica fallará:
# mezclado * 0.19   →  TypeError: ufunc 'multiply' did not contain a loop
```

Cuando NumPy recibe valores de tipos distintos, intenta convertirlos todos al tipo más general. Si hay un string en el lote, todo se convierte a string y pierdes la capacidad de operar numéricamente. Por eso `NITS` se queda como lista Python separada, sin mezclarla con `VALORES_DECLARADOS`.

### Datos de práctica

Abre `src/numpy_utils.py`. Al inicio encontrarás los datos de esta sesión:

```python
VALORES_DECLARADOS = np.array([
    1_500_000,
    850_000,
    0,
    2_300_000,
    950_000,
    3_200_000,
    450_000,
    1_100_000,
], dtype=np.float64)

DIAS_MORA = np.array([0, 30, 0, 45, 90, 0, 120, 15], dtype=np.int32)

NITS = [
    "900123456", "800234567", "700345678", "600456789",
    "500567890", "400678901", "300789012", "200890123",
]
```

`NITS` sigue siendo una lista Python porque los identificadores de texto no se benefician de NumPy.

### Pausa y piensa 💭

> Antes de continuar, intenta responder estas preguntas mirando solo los datos de práctica arriba:
>
> 1. ¿Cuántos contribuyentes no tienen mora (`DIAS_MORA == 0`)? Cuéntalos a ojo.
> 2. ¿Cuál es el valor declarado más alto? ¿Y el más bajo que no sea cero?
> 3. Si tuvieras que filtrar los registros con mora mayor a 60 días, ¿qué índices del array necesitarías?
>
> Anota tus respuestas. Cuando implementes las funciones de las secciones 5 y 6, podrás verificar si acertaste.

### Funciones a implementar

#### `describir_array(arr)`

Esta función es un **procedimiento de diagnóstico**: recibe cualquier array y muestra sus características básicas. Es la primera herramienta que ejecutarás cuando recibas un nuevo conjunto de datos. Antes de calcular nada, conviene saber qué forma tiene, qué tipo de datos guarda y cuál es su rango de valores.

```python
def describir_array(arr):
    """
    Imprime la forma, el tipo de dato, el mínimo y el máximo de un array.

    Es un procedimiento: no retorna ningún valor.

    Args:
        arr (np.ndarray): Array de NumPy a describir.

    Ejemplo de salida con VALORES_DECLARADOS:
        Forma   : (8,)
        Tipo    : float64
        Mínimo  : 0.0
        Máximo  : 3200000.0
    """
```

Implementación:

```python
def describir_array(arr):
    print(f"  Forma   : {arr.shape}")
    print(f"  Tipo    : {arr.dtype}")
    print(f"  Mínimo  : {arr.min()}")
    print(f"  Máximo  : {arr.max()}")
```

Nota que `arr.min()` y `arr.max()` son **métodos del array**, funciones que viven dentro del objeto ndarray y tienen acceso directo a sus datos. También podrías escribir `np.min(arr)` y `np.max(arr)` con el mismo resultado; ambas formas son correctas.

#### `crear_array_declaraciones(valores_lista)`

```python
def crear_array_declaraciones(valores_lista):
    """
    Convierte una lista de Python en un array NumPy de tipo float64.

    Args:
        valores_lista (list): Lista de números.

    Returns:
        np.ndarray: Array de NumPy con dtype float64.

    Ejemplo:
        crear_array_declaraciones([1_000_000, 500_000, 2_000_000])
        -> array([1000000., 500000., 2000000.])
    """
```

Implementación:

```python
def crear_array_declaraciones(valores_lista):
    return np.array(valores_lista, dtype=np.float64)
```

#### `comparar_lista_vs_array(valores_lista)`

Esta función es solo ilustrativa: muestra la diferencia entre trabajar con listas y con arrays.

```python
def comparar_lista_vs_array(valores_lista):
    # Con lista: necesitamos un ciclo
    iva_lista = []
    for valor in valores_lista:
        iva_lista.append(valor * 0.19)

    # Con array: operación directa sobre todos los elementos
    arr = np.array(valores_lista, dtype=np.float64)
    iva_array = arr * 0.19

    print("  Lista (requiere ciclo for):")
    print(f"    {iva_lista}")
    print("  Array (operación directa):")
    print(f"    {iva_array}")
```

#### `filtrar_valores_en_rango(valores_lista, minimo, maximo)`

Esta función retoma el ejercicio de listas para recorrer una lista con un ciclo y un condicional para quedarte solo con los valores dentro de un rango. Verla aquí, antes de los arrays booleanos de la sección 5, te deja comparar de primera mano cómo cambia el mismo problema cuando lo resuelves con NumPy.

```python
def filtrar_valores_en_rango(valores_lista, minimo, maximo):
    """
    Retorna una lista nueva con los valores que están entre minimo y maximo.

    Recorre la lista con un ciclo for y usa un condicional para decidir
    si cada valor entra en el rango.

    Args:
        valores_lista (list): Lista de números a filtrar.
        minimo (float): Límite inferior del rango (incluido).
        maximo (float): Límite superior del rango (incluido).

    Returns:
        list: Valores que cumplen minimo <= valor <= maximo.

    Ejemplo:
        filtrar_valores_en_rango([100, 500, 1200, 30], 100, 1000)
        -> [100, 500]
    """
```

Implementación:

```python
def filtrar_valores_en_rango(valores_lista, minimo, maximo):
    filtrados = []
    for valor in valores_lista:
        if minimo <= valor <= maximo:
            filtrados.append(valor)
    return filtrados
```

Guarda esta lógica en la cabeza: en la sección 5 vas a resolver exactamente el mismo problema, filtrar por rango, sin escribir el ciclo `for` ni el `if`.

### Verificar en main.py

Una vez implementadas las cuatro funciones, abre `main.py` y descomenta los bloques dentro de `menu_arrays_y_tipos()`. Luego ejecuta:

```bash
python main.py
```

Selecciona opción `1` y verifica la salida.

## 🔁 Ciclo Git

```bash
git add src/numpy_utils.py
git commit -m "sesion-04: sec-1 arrays y tipos de datos"
git push
```

---
## Sección 2 — Indexación y slicing

### Indexación básica

Acceder a un elemento por su posición funciona igual que con listas de Python. Las posiciones empiezan en **cero**, no en uno:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
#               ↑   ↑   ↑   ↑   ↑
# posición:     0   1   2   3   4

print(arr[0])   # 10  ← primer elemento (posición 0)
print(arr[2])   # 30  ← tercer elemento (posición 2)
print(arr[4])   # 50  ← último elemento (posición 4)
```

También puedes contar desde el final usando posiciones negativas:

```python
print(arr[-1])  # 50  ← último elemento
print(arr[-2])  # 40  ← penúltimo elemento
print(arr[-5])  # 10  ← equivale a arr[0] en un array de 5 elementos
```

La regla es: `arr[-n]` es lo mismo que `arr[len(arr) - n]`. Así, `arr[-1]` es `arr[4]` para un array de 5 elementos.

> **Escalar NumPy:** cuando indexas un array NumPy obtienes un **escalar NumPy** (por ejemplo `np.float64(1500000.0)`), no un número Python común (`1500000.0`). En la práctica se comportan igual en cálculos, pero si en algún momento ves `np.float64(...)` en la salida no te alarmes, es el tipo nativo de NumPy y funciona normalmente en cualquier operación aritmética.

### Punto de fallo #3 — IndexError: índice fuera de rango

```python
arr = np.array([10, 20, 30, 40, 50])  # 5 elementos, posiciones 0 a 4

print(arr[5])   # IndexError: index 5 is out of bounds for axis 0 with size 5
```

El error ocurre porque el último índice válido es `4`, no `5`. Un array de `n` elementos tiene posiciones `0` a `n-1`. Si ves este error, verifica cuántos elementos tiene tu array con `len(arr)` o `arr.shape[0]` antes de indexar.

### Slicing — acceder a un rango de elementos

El **slicing** (rebanado) permite extraer un fragmento del array especificando el inicio y el fin de la selección:

```
arr[inicio : fin]
```

El `inicio` es **inclusivo** (se incluye) y el `fin` es **exclusivo** (no se incluye). Esto es consistente con `range(inicio, fin)` que ya conoces de los ciclos `for`.

```python
arr = np.array([100, 200, 300, 400, 500])
#               ↑    ↑    ↑    ↑    ↑
# posición:     0    1    2    3    4

print(arr[1:4])   # [200 300 400]  ← posiciones 1, 2 y 3 (el 4 no se incluye)
print(arr[0:3])   # [100 200 300]  ← posiciones 0, 1 y 2
```

> **¿Por qué el fin es exclusivo?**  
> Es una convención de Python y NumPy. La ventaja práctica: `arr[1:4]` siempre tiene exactamente `4 - 1 = 3` elementos. No tienes que restar 1 para calcular la longitud del fragmento.

Si omites el inicio o el fin, NumPy asume el extremo del array:

```python
print(arr[:3])    # [100 200 300]  ← desde el inicio hasta posición 2
print(arr[2:])    # [300 400 500]  ← desde posición 2 hasta el final
print(arr[:])     # [100 200 300 400 500]  ← el array completo
```

### Slicing con índices negativos y paso

Puedes combinar índices negativos con slicing:

```python
arr = np.array([100, 200, 300, 400, 500])

print(arr[-3:])   # [300 400 500]  ← últimos 3 elementos
print(arr[:-2])   # [100 200 300]  ← todo excepto los últimos 2
```

El tercer parámetro opcional es el **paso**: cuántas posiciones saltar entre cada elemento seleccionado.

```
arr[inicio : fin : paso]
```

```python
print(arr[::2])   # [100 300 500]  ← uno de cada dos (posiciones 0, 2, 4)
print(arr[1::2])  # [200 400]      ← empezando en 1, uno de cada dos
print(arr[::-1])  # [500 400 300 200 100]  ← paso -1: recorre el array al revés
```

`arr[::-1]` es la forma idiomática de invertir un array en NumPy: sin inicio ni fin (toma todo), con paso `-1` (de derecha a izquierda).

### Vista vs copia

Cuando haces slicing de un array NumPy, el resultado es una **vista**, una ventana sobre los mismos datos en memoria. Modificar la vista modifica también el array original.

```python
arr = np.array([100, 200, 300, 400, 500])
vista = arr[1:4]       # vista apunta a posiciones 1, 2, 3 de arr

print(vista)           # [200 300 400]
vista[0] = 999         # modifico el primer elemento de la vista

print(vista)           # [999 300 400]
print(arr)             # [100 999 300 400 500]  ← arr también cambió
```

En las listas de Python, un slice sí crea una copia independiente. En NumPy no. Si necesitas un array completamente independiente, usa `.copy()`:

```python
copia = arr[1:4].copy()
copia[0] = 0

print(arr)   # [100 999 300 400 500]  ← arr no cambió
```

### Punto de fallo #4 — modificar una vista sin darse cuenta

Este es el error que más duele: el código corre limpio y los datos cambian sin ningún aviso.

```python
import numpy as np

declaraciones = np.array([1_500_000, 850_000, 0, 2_300_000, 950_000], dtype=np.float64)

# "Solo voy a trabajar con las primeras tres declaraciones"
primeras_tres = declaraciones[:3]

# Aplico un ajuste temporal
primeras_tres[2] = 999_999   # quería modificar solo mi subarray

print(declaraciones)
# [1500000.  850000. 999999. 2300000.  950000.]  ← ¡el original cambió!
```

**Regla práctica:** si vas a modificar un subarray o pasarlo a una función que lo modifique, usa `.copy()`. Si solo vas a leer (filtrar, calcular), la vista es eficiente y está bien usarla.

### Pausa y piensa 💭

> Dado `VALORES_DECLARADOS = np.array([1_500_000, 850_000, 0, 2_300_000, 950_000, 3_200_000, 450_000, 1_100_000])`:
>
> Predice el resultado de cada expresión **antes** de ejecutarla:
> 1. `VALORES_DECLARADOS[3]`
> 2. `VALORES_DECLARADOS[-2]`
> 3. `VALORES_DECLARADOS[2:5]`
> 4. `VALORES_DECLARADOS[::3]`
>
> Luego ejecuta y compara. ¿En cuáles acertaste? ¿En cuáles te sorprendió el resultado y por qué?

### Funciones a implementar

#### `obtener_rango(arr, inicio, fin)`

```python
def obtener_rango(arr, inicio, fin):
    """
    Retorna los elementos del array entre las posiciones inicio y fin (excluido).

    Args:
        arr (np.ndarray): Array de NumPy.
        inicio (int): Posición inicial (inclusive).
        fin (int): Posición final (exclusiva).

    Returns:
        np.ndarray: Subarray con los elementos del rango.

    Ejemplo:
        obtener_rango(VALORES_DECLARADOS, 2, 5)
        -> array([      0., 2300000.,  950000.])
    """
```

Implementación:

```python
def obtener_rango(arr, inicio, fin):
    return arr[inicio:fin]
```

#### `obtener_ultimos(arr, n)`

```python
def obtener_ultimos(arr, n):
    """
    Retorna los últimos n elementos del array.

    Args:
        arr (np.ndarray): Array de NumPy.
        n (int): Número de elementos a retornar desde el final.

    Returns:
        np.ndarray: Subarray con los últimos n elementos.
    """
```

Implementación:

```python
def obtener_ultimos(arr, n):
    return arr[-n:]
```

#### `invertir_array(arr)`

```python
def invertir_array(arr):
    """
    Retorna una copia del array con los elementos en orden invertido.

    Args:
        arr (np.ndarray): Array de NumPy.

    Returns:
        np.ndarray: Array con elementos en orden invertido.
    """
```

Implementación:

```python
def invertir_array(arr):
    return arr[::-1]
```

### Verificar en main.py

Descomenta los bloques dentro de `menu_indexacion_slicing()` y ejecuta `python main.py`, opción `2`.

### Ejercicios — Sección 2

**Básico:** ¿Cuál es el resultado de `VALORES_DECLARADOS[::2]`? ¿Y de `VALORES_DECLARADOS[1::2]`? ¿Qué patrón ves?

**Intermedio:** Usando solo slicing (sin ciclos), obtén los valores del índice 1 al 5 en orden invertido a partir de `VALORES_DECLARADOS`.

**Avanzado:** `obtener_rango` devuelve una vista. ¿Qué pasaría si hicieras `rango = obtener_rango(VALORES_DECLARADOS, 0, 3)` y luego `rango[0] = 999`? Pruébalo. ¿Cómo lo prevendrías?

### Commit de sección

```bash
git add src/numpy_utils.py
git commit -m "sesion-04: sec-2 indexacion y slicing"
git push
```

---

## Pausa

**⏱ 15 min**

---
## Sección 3 — Vectorización

**⏱ Tiempo estimado: 25 min**

### ¿Qué es la vectorización?

Vectorizar una operación significa expresarla de forma que se aplique a todos los elementos de un array a la vez, sin ciclo explícito. En lugar de iterar uno por uno en Python, NumPy delega el cálculo a código escrito en **C**, ya compilado y listo para ejecutarse directamente en el procesador.

### ¿Qué es C?

**C** es un lenguaje de programación creado en 1972 en los laboratorios Bell de AT&T. Es uno de los lenguajes más antiguos que todavía se usan activamente, y también uno de los más rápidos.

Para entender por qué, hay que distinguir dos formas en que un computador puede ejecutar código:

| Modo | Ejemplo | Cómo funciona |
|---|---|---|
| **Interpretado** | Python | Lee y ejecuta el código línea por línea, en tiempo real |
| **Compilado** | C | Traduce todo el código a instrucciones del procesador *antes* de ejecutarlo |

Cuando Python ejecuta `valor * 0.19` en un ciclo, en cada elemento tiene que verificar el tipo de `valor`, buscar la operación de multiplicación para ese tipo, ejecutarla y guardar el resultado. Ese proceso ocurre uno por uno.

Cuando C hace lo mismo, ya tiene las instrucciones del procesador listas. No verifica tipos en tiempo de ejecución, no busca nada. Ejecuta directamente, a la velocidad del hardware.

La analogía: tienes que sellar 10.000 sobres.

- Con Python puro: le explicas a alguien cómo sellar un sobre, esperas que lo haga, le explicas el siguiente, esperas...
- Con NumPy y C por debajo: le das a una máquina selladora el lote completo y la pones a correr.

El núcleo de NumPy está escrito en C. Cuando escribes `arr * 0.19`, Python le pasa el array completo a funciones C ya compiladas, que ejecutan la operación sobre todos los elementos en una sola pasada y devuelven el resultado. Tú escribes Python; el trabajo pesado lo hace C.

> **Nota:** no necesitas aprender C para usar NumPy. Solo necesitas saber que está ahí, haciendo el trabajo rápido para que tú puedas escribir código legible.

Además de usar C, NumPy guarda los datos en **memoria contigua**: todos los valores del array están uno al lado del otro en la RAM, sin saltos. Una lista de Python, en cambio, guarda referencias dispersas: la dirección de memoria de cada elemento. El procesador tiene que ir a buscar cada valor por separado. Con un array contiguo, puede cargar varios valores a la vez en su caché y operar sobre ellos en paralelo.

### Benchmark: ver la diferencia con tus propios ojos

Antes de implementar las funciones, ejecuta este script para medir la diferencia real entre las dos formas de calcular el IVA de un millón de declaraciones:

```python
import time
import numpy as np

N = 1_000_000
lista = []
for i in range(N):
    lista.append(float(i * 1000))

arr = np.array(lista, dtype=np.float64)

# --- Con ciclo for sobre lista ---
inicio = time.time()
iva_lista = []
for valor in lista:
    iva_lista.append(valor * 0.19)
tiempo_lista = time.time() - inicio

# --- Con vectorización NumPy ---
inicio = time.time()
iva_array = arr * 0.19
tiempo_numpy = time.time() - inicio

print(f"Lista + ciclo for : {tiempo_lista:.4f} s")
print(f"Array NumPy       : {tiempo_numpy:.4f} s")
print(f"NumPy es {tiempo_lista / tiempo_numpy:.0f}x más rápido")
```

Salida típica (puede variar según el equipo):

```
Lista + ciclo for : 0.0821 s
Array NumPy       : 0.0018 s
NumPy es 46x más rápido
```

> **¿Por qué importa?**  
> Un archivo de declaraciones puede tener varios millones de registros. Si cada operación tarda 80 ms con ciclo y 2 ms con NumPy, la diferencia total en un pipeline completo de 20 operaciones es la diferencia entre esperar 1,6 segundos o 40 milisegundos, en cada ejecución, varias veces al día.

### Operaciones aritméticas vectorizadas

Todas las operaciones aritméticas (`+`, `-`, `*`, `/`, `**`) aplican elemento a elemento cuando se usan con arrays:

```python
import numpy as np

valores = np.array([1_000_000, 500_000, 2_000_000], dtype=np.float64)

# Escalar × array: multiplica cada elemento
iva = valores * 0.19
print(iva)   # [190000.  95000. 380000.]

# Array + escalar
con_iva = valores + iva
print(con_iva)   # [1190000.  595000. 2380000.]

# Dos arrays del mismo tamaño: opera par a par
factor = np.array([1.0, 0.9, 1.1])
ajustados = valores * factor
print(ajustados)   # [1000000.  450000. 2200000.]
```

### Cuando el resultado no cuadra: verificar con muestra manual

La velocidad de NumPy tiene un costo de visibilidad: una operación que procesa miles de registros no te muestra qué hizo con cada uno. Si el resultado parece incorrecto, valores negativos donde no deberían existir, totales que no cierran, `nan` inesperados, el ciclo `for` de sesión 3 es la herramienta de diagnóstico que necesitas.

El patrón es siempre el mismo:

1. Toma una muestra pequeña (3 a 5 elementos).
2. Implementa la lógica que *esperas* con un ciclo `for` explícito.
3. Compara cada posición contra lo que devolvió NumPy.

Ejemplo: supón que `calcular_sanciones_vectorizadas` (la implementarás en la sección 6) devuelve valores que no cuadran. Así lo diagnosticarías:

```python
import numpy as np

sanciones = calcular_sanciones_vectorizadas(VALORES_DECLARADOS, DIAS_MORA)

for i in range(4):
    valor = VALORES_DECLARADOS[i]
    dias  = int(DIAS_MORA[i])
    resultado_numpy = sanciones[i]

    # Misma lógica de tramos, escrita a mano con if/elif
    if dias == 0:
        tasa = 0.0
    elif dias <= 30:
        tasa = 0.01
    elif dias <= 90:
        tasa = 0.05
    else:
        tasa = 0.10
    resultado_manual = valor * tasa

    # Comparación explícita
    if abs(resultado_numpy - resultado_manual) < 0.01:
        estado = "OK"
    else:
        estado = "DIFERENTE"

    print(
        f"  [{i}] dias={dias:>3} | "
        f"manual={resultado_manual:>10,.0f} | "
        f"numpy={resultado_numpy:>10,.0f} | {estado}"
    )
```

Si los resultados coinciden en los primeros 4, el problema probablemente está en los datos de entrada, no en la lógica. Si difieren, la discrepancia señala exactamente en qué tramo está el error.

> **Regla práctica:** cuando un resultado vectorizado no tiene sentido, reduce a 3 elementos y recorre la lógica a mano. Ese ciclo `for` es temporal y nunca va al código final, pero sí te desbloquea.

### Funciones a implementar

#### `calcular_iva_todos(valores, tasa=0.19)`

```python
def calcular_iva_todos(valores, tasa=0.19):
    """
    Calcula el IVA sobre cada valor declarado en el array.

    En sesión 3 hacíamos esto con un ciclo for. Con NumPy, la multiplicación
    opera sobre todos los elementos simultáneamente.

    Args:
        valores (np.ndarray): Array de valores declarados.
        tasa (float): Tasa de IVA. Por defecto 0.19.

    Returns:
        np.ndarray: Array con el IVA calculado para cada elemento.

    Ejemplo:
        calcular_iva_todos(np.array([1_000_000, 500_000]))
        -> array([190000.,  95000.])
    """
```

Implementación:

```python
def calcular_iva_todos(valores, tasa=0.19):
    return valores * tasa
```

#### `calcular_valor_con_iva(valores, tasa=0.19)`

```python
def calcular_valor_con_iva(valores, tasa=0.19):
    """
    Calcula el valor total incluyendo IVA para cada elemento del array.

    Args:
        valores (np.ndarray): Array de valores base.
        tasa (float): Tasa de IVA. Por defecto 0.19.

    Returns:
        np.ndarray: Array con el valor base más el IVA.

    Ejemplo:
        calcular_valor_con_iva(np.array([1_000_000, 500_000]))
        -> array([1190000.,  595000.])
    """
```

Implementación:

```python
def calcular_valor_con_iva(valores, tasa=0.19):
    factor_con_iva = 1 + tasa
    return valores * factor_con_iva
```

> **¿Por qué `factor_con_iva = 1 + tasa` es mejor que `valores + valores * tasa`?**
> La primera forma recorre el array una sola vez, y de paso le pone nombre a lo que representa el número: el factor por el que se multiplica el valor base para obtener el valor con IVA incluido. La segunda forma recorre el array dos veces y no deja ningún rastro de qué significa la operación. Para arrays grandes, además, la diferencia de rendimiento es apreciable.

#### `redondear_a_miles(arr)`

En tributario, los valores suelen redondearse al múltiplo de 1.000 más cercano para coincidir con formularios.

```python
def redondear_a_miles(arr):
    """
    Redondea cada valor al múltiplo de 1000 más cercano.

    Args:
        arr (np.ndarray): Array de valores numéricos.

    Returns:
        np.ndarray: Array con valores redondeados a miles.

    Ejemplo:
        redondear_a_miles(np.array([1_234_567, 890_123]))
        -> array([1235000.,  890000.])
    """
```

Implementación:

```python
def redondear_a_miles(arr):
    valor_en_miles = arr / 1000
    miles_redondeados = np.round(valor_en_miles)
    return miles_redondeados * 1000
```

Tres pasos en vez de uno: dividir, redondear, multiplicar de vuelta. Nombrar cada resultado intermedio deja claro qué hace cada operación, en lugar de obligar a leer la expresión completa antes de entender qué representa.

### Verificar en main.py

Descomenta los bloques dentro de `menu_vectorizacion()` y ejecuta `python main.py`, opción `3`.

La salida de `calcular_iva_todos` debería verse así:

```
  IVA por declaración:
  900123456 | $   1,500,000 | IVA: $    285,000
  800234567 | $     850,000 | IVA: $    161,500
  700345678 | $           0 | IVA: $          0
  ...
```

### Pausa y piensa 💭

> En sesión 3 implementaste `calcular_totales` usando un ciclo `for`. ¿Puedes reescribir esa función en una sola línea usando NumPy? ¿Cuándo preferirías la versión con ciclo y cuándo la versión vectorizada?

### Ejercicios — Sección 3

**Básico:** Calcula el valor total de todas las declaraciones con `VALORES_DECLARADOS.sum()`. Luego calcula el promedio con `.mean()`. ¿Coincide el promedio con lo que esperarías a ojo?

**Intermedio:** Implementa `calcular_retencion(valores, tasa=0.035)` que calcule la retención en la fuente (3.5 %) para cada declaración usando vectorización.

**Avanzado:** ¿Qué ocurre si `tasa` es un array de la misma longitud que `valores`? Crea `tasas = np.array([0.19, 0.05, 0.0, 0.19, 0.05, 0.19, 0.0, 0.05])` y pásalo como `tasa` a `calcular_iva_todos`. ¿Funciona? ¿Por qué NumPy permite esto?

### Commit de sección

```bash
git add src/numpy_utils.py
git commit -m "sesion-04: sec-3 vectorizacion"
git push
```

---
## Sección 4 — Funciones universales (ufuncs)

**⏱ Tiempo estimado: 25 min**

### ¿Qué son las ufuncs?

Las **ufuncs** (universal functions) son funciones de NumPy que operan elemento a elemento sobre arrays. Cubren operaciones matemáticas sin operador propio: valor absoluto, raíz cuadrada, logaritmo, etc.

```python
import numpy as np

arr = np.array([-3.0, -1.0, 0.0, 2.0, 5.0])
print(np.abs(arr))       # [3. 1. 0. 2. 5.]

arr_pos = np.array([0.0, 1.0, 4.0, 9.0, 16.0])
print(np.sqrt(arr_pos))  # [0. 1. 2. 3. 4.]
```

También puedes combinar dos arrays:

```python
a = np.array([1_000_000, 2_000_000, 3_000_000], dtype=np.float64)
b = np.array([900_000, 2_100_000, 2_800_000], dtype=np.float64)

print(np.abs(a - b))     # [100000. 100000. 200000.]
print(np.maximum(a, b))  # [1000000. 2100000. 3000000.]
```

### Punto de fallo #5 — np.sqrt sobre valores negativos

```python
import numpy as np

arr = np.array([1_000_000, 4_000_000, -500_000], dtype=np.float64)
resultado = np.sqrt(arr)
print(resultado)
# [1000.     2000.       nan]
# RuntimeWarning: invalid value encountered in sqrt
```

NumPy devuelve `nan` (Not a Number) para los valores negativos, sin lanzar excepción, y emite una advertencia. El programa sigue corriendo, lo que puede propagar valores inválidos silenciosamente. En datos monetarios, un valor negativo en `VALORES_DECLARADOS` podría indicar un error de carga. Siempre verifica con `np.any(arr < 0)` antes de aplicar `np.sqrt`.

### Funciones a implementar

#### `calcular_variacion_absoluta(valores_actuales, valores_anteriores)`

Esta función responde la pregunta: ¿cuánto cambió cada declaración respecto al período anterior, sin importar si subió o bajó?

```python
def calcular_variacion_absoluta(valores_actuales, valores_anteriores):
    """
    Calcula la variación absoluta entre dos períodos para cada registro.

    Args:
        valores_actuales (np.ndarray): Valores del período actual.
        valores_anteriores (np.ndarray): Valores del período anterior.

    Returns:
        np.ndarray: Array con la variación absoluta de cada elemento.

    Ejemplo:
        calcular_variacion_absoluta(
            np.array([1_200_000, 800_000, 300_000]),
            np.array([1_000_000, 900_000, 300_000])
        )
        -> array([200000., 100000.,      0.])
    """
```

Implementación:

```python
def calcular_variacion_absoluta(valores_actuales, valores_anteriores):
    return np.abs(valores_actuales - valores_anteriores)
```

Sin `np.abs`, una declaración que bajó de 900.000 a 800.000 daría `-100.000`. El valor absoluto convierte eso en `100.000`, la magnitud del cambio independientemente de la dirección.

#### `normalizar_valores(arr)`

La normalización min-max escala todos los valores al rango [0, 1]. Es útil cuando quieres comparar declaraciones de distintas magnitudes en la misma escala: el valor mínimo siempre queda en 0.0 y el máximo en 1.0, y todos los demás se ubican proporcionalmente entre ellos.

```python
def normalizar_valores(arr):
    """
    Escala los valores al rango [0, 1] usando normalización min-max.

    La fórmula es: (valor - mínimo) / (máximo - mínimo).
    Un valor de 0.0 corresponde al mínimo y 1.0 al máximo.

    Args:
        arr (np.ndarray): Array de valores numéricos. No debe tener todos
                          los elementos iguales (división por cero).

    Returns:
        np.ndarray: Array con valores normalizados entre 0 y 1.

    Ejemplo:
        normalizar_valores(np.array([0, 1_000_000, 2_000_000]))
        -> array([0. , 0.5, 1. ])
    """
```

Implementación:

```python
def normalizar_valores(arr):
    minimo = arr.min()
    maximo = arr.max()
    return (arr - minimo) / (maximo - minimo)
```

> **¿Por qué variables separadas para `minimo` y `maximo`?**  
> Si escribieras `(arr - arr.min()) / (arr.max() - arr.min())`, NumPy recorrería el array tres veces (una por cada llamada a `.min()` y `.max()`). Guardando los resultados en variables, lo recorre dos veces. Para millones de registros, esta diferencia es medible.

#### `aplicar_raiz_cuadrada(arr)`

```python
def aplicar_raiz_cuadrada(arr):
    """
    Calcula la raíz cuadrada de cada elemento del array.

    Útil para transformar distribuciones sesgadas antes de comparar valores.

    Args:
        arr (np.ndarray): Array de valores no negativos.

    Returns:
        np.ndarray: Array con la raíz cuadrada de cada elemento.
    """
```

Implementación:

```python
def aplicar_raiz_cuadrada(arr):
    return np.sqrt(arr)
```

### Verificar en main.py

Descomenta los bloques dentro de `menu_ufuncs()` y ejecuta `python main.py`, opción `4`.

### Pausa y piensa 💭

> `normalizar_valores` divide por `(maximo - minimo)`. ¿Qué ocurre si todos los valores del array son exactamente iguales? El denominador sería cero y obtendrías `nan`. ¿Cómo detectarías ese caso antes de calcular? Escribe la condición de guarda que agregarías al inicio de la función.

### Ejercicios — Sección 4

**Básico:** ¿Qué devuelve `np.sqrt(np.array([0.0, 4.0, 9.0, -1.0]))`? ¿Qué ocurre con el valor negativo? ¿Es un error o un valor especial de NumPy?

**Intermedio:** Usa `normalizar_valores` sobre `VALORES_DECLARADOS`. ¿Qué NIT tiene el valor normalizado más cercano a 0.5 (la "declaración media")?

**Avanzado:** Investiga `np.log1p`. ¿Cuál es la diferencia entre `np.log(x)` y `np.log1p(x)` cuando `x = 0`? ¿Por qué `np.log1p` es más segura en datos donde puede haber declaraciones en cero?

### Commit de sección

```bash
git add src/numpy_utils.py
git commit -m "sesion-04: sec-4 ufuncs"
git push
```

---
## Sección 5 — Arrays booleanos

**⏱ Tiempo estimado: 25 min**

### Las comparaciones producen arrays

Imagina que tienes 8 declaraciones y necesitas saber cuáles tienen mora. Con un ciclo harías algo así:

```python
dias = [0, 30, 0, 45, 90, 0, 120, 15]
en_mora = []
for d in dias:
    if d > 0:
        en_mora.append(True)
    else:
        en_mora.append(False)
```

NumPy reduce eso a una línea. Cuando aplicas un operador de comparación a un array, Python devuelve un **array entero de booleanos**, uno por cada elemento:

```python
import numpy as np

dias = np.array([0, 30, 0, 45, 90, 0, 120, 15], dtype=np.int32)

en_mora = dias > 0
print(en_mora)
# [False  True False  True  True False  True  True]
print(type(en_mora))   # <class 'numpy.ndarray'>
print(en_mora.dtype)   # bool
```

Cada posición responde la pregunta "¿este elemento cumple la condición?" de forma independiente. A este array de `True`/`False` se le llama **máscara booleana** porque, como una máscara, cubre los elementos que no cumplen y deja visibles solo los que sí.

### Filtrar con la máscara

La máscara lista es el paso previo. Con ella puedes extraer directamente los elementos que cumplen la condición:

```python
valores = np.array([1_500_000, 850_000, 0, 2_300_000,
                    950_000, 3_200_000, 450_000, 1_100_000], dtype=np.float64)
dias    = np.array([0, 30, 0, 45, 90, 0, 120, 15], dtype=np.int32)

# Paso 1: crear la máscara
mascara_mora = dias > 0
print(mascara_mora)
# [False  True False  True  True False  True  True]

# Paso 2: usar la máscara como índice
valores_en_mora = valores[mascara_mora]
print(valores_en_mora)
# [ 850000. 2300000.  950000.  450000. 1100000.]
```

NumPy selecciona los elementos donde la máscara es `True` y descarta los que son `False`. El resultado es un nuevo array que solo contiene los valores que cumplen la condición.

Puedes hacer los dos pasos en una sola línea:

```python
print(valores[dias > 0])
# [ 850000. 2300000.  950000.  450000. 1100000.]
```

Usar la variable `mascara_mora` es más legible y facilita depurar: puedes imprimir la máscara antes de filtrar para verificar que seleccionó los elementos correctos.

### Contar con np.sum

`True` vale `1` y `False` vale `0` en operaciones numéricas. Por eso `np.sum` sobre una máscara cuenta los `True`. Una línea.

```python
mascara = dias > 0
print(np.sum(mascara))    # 5 ← cinco registros con mora
print(mascara.sum())      # 5 ← equivalente (método del array)
print(np.mean(mascara))   # 0.625 ← 62.5% de los registros tienen mora
```

### Punto de fallo #6 — usar `and` en lugar de `&` al combinar condiciones

Esto le pasa a casi todo el mundo la primera vez:

```python
dias   = np.array([0, 30, 0, 45, 90, 0, 120, 15], dtype=np.int32)
valores = np.array([1_500_000, 850_000, 0, 2_300_000,
                    950_000, 3_200_000, 450_000, 1_100_000], dtype=np.float64)

# INCORRECTO — 'and' no funciona con arrays
# filtrado = valores[(dias > 0) and (valores > 500_000)]
# ValueError: The truth value of an array with more than one element is ambiguous

# CORRECTO — usar & para AND, | para OR
filtrado = valores[(dias > 0) & (valores > 500_000)]
print(filtrado)
# [ 850000. 2300000.  950000. 1100000.]
```

`and` y `or` de Python trabajan con un solo valor booleano. Para combinar dos máscaras se usan los operadores bitwise `&` (AND) y `|` (OR). Los paréntesis alrededor de cada condición son obligatorios: sin ellos, Python interpreta la expresión en el orden incorrecto.

### Funciones a implementar

#### `obtener_mascara_mora(dias_mora)`

```python
def obtener_mascara_mora(dias_mora):
    """
    Retorna un array booleano que indica qué registros tienen mora.

    Args:
        dias_mora (np.ndarray): Array con los días de mora por registro.

    Returns:
        np.ndarray: Array de booleanos, True donde dias_mora > 0.

    Ejemplo:
        obtener_mascara_mora(np.array([0, 30, 0, 45]))
        -> array([False,  True, False,  True])
    """
```

Implementación:

```python
def obtener_mascara_mora(dias_mora):
    return dias_mora > 0
```

#### `filtrar_valores_con_mora(valores, dias_mora)`

```python
def filtrar_valores_con_mora(valores, dias_mora):
    """
    Retorna los valores declarados de los registros que tienen mora.

    Args:
        valores (np.ndarray): Array de valores declarados.
        dias_mora (np.ndarray): Array con los días de mora.

    Returns:
        np.ndarray: Subarray con solo los valores de registros en mora.

    Ejemplo:
        filtrar_valores_con_mora(
            np.array([1_500_000, 850_000, 0, 2_300_000]),
            np.array([0, 30, 0, 45])
        )
        -> array([ 850000., 2300000.])
    """
```

Implementación:

```python
def filtrar_valores_con_mora(valores, dias_mora):
    mascara = dias_mora > 0
    return valores[mascara]
```

#### `contar_sobre_umbral(arr, umbral)`

```python
def contar_sobre_umbral(arr, umbral):
    """
    Cuenta cuántos elementos del array superan el umbral indicado.

    Args:
        arr (np.ndarray): Array de valores numéricos.
        umbral (float): Valor de referencia.

    Returns:
        int: Número de elementos mayores que umbral.

    Ejemplo:
        contar_sobre_umbral(VALORES_DECLARADOS, 1_000_000)
        -> 4
    """
```

Implementación:

```python
def contar_sobre_umbral(arr, umbral):
    mascara = arr > umbral
    cantidad = np.sum(mascara)
    return int(cantidad)
```

Separar `mascara` de `cantidad` hace explícitos los dos pasos del problema: primero decidir qué elementos cuentan, después contarlos. El `int(...)` final convierte el resultado de `np.int64` a un entero Python estándar. Es una buena práctica cuando el resultado se usará fuera de NumPy.

### Verificar en main.py

Descomenta los bloques dentro de `menu_boolean_arrays()` y ejecuta `python main.py`, opción `5`.

Salida esperada de `filtrar_valores_con_mora`:

```
  Valores declarados con mora:
    $850,000
    $2,300,000
    $950,000
    $450,000
    $1,100,000
  Total en riesgo: $5,650,000
```

### Pausa y piensa 💭

> En la sección 1 de esta misma sesión implementaste `filtrar_valores_en_rango` con un ciclo `for` que acumulaba resultados en una lista. Ahora tienes máscaras booleanas. Escribe mentalmente cómo sería la versión NumPy de esa función en una sola línea. ¿Cuál de las dos versiones es más fácil de leer y por qué?

### Ejercicios — Sección 5

**Básico:** ¿Cuántos registros en `DIAS_MORA` tienen exactamente 0 días de mora? Usa `np.sum(DIAS_MORA == 0)`.

**Intermedio:** Combina dos condiciones: filtra los valores donde `dias_mora > 0` AND `valores > 500_000`. Usa `(DIAS_MORA > 0) & (VALORES_DECLARADOS > 500_000)`. ¿Cuántos registros cumplen ambas?

**Avanzado:** Usa `np.where(mascara)` sin segundo ni tercer argumento. ¿Qué devuelve? ¿Cómo usarías ese resultado para obtener los NIT de los contribuyentes en mora a partir de la lista `NITS`?

### Commit de sección

```bash
git add src/numpy_utils.py
git commit -m "sesion-04: sec-5 arrays booleanos"
git push
```

---
## Sección 6 — np.where

**⏱ Tiempo estimado: 30 min**

### ¿Qué hace np.where?

`np.where(condicion, valor_si_true, valor_si_false)` construye un nuevo array recorriendo la condición elemento a elemento: donde la condición es `True` toma el primer valor; donde es `False` toma el segundo.

Es el equivalente vectorizado de `if/else`. Opera sobre todos los elementos a la vez, sin ciclo:

```python
# Con if/else necesitarías un ciclo:
# resultado = []
# for v in valores:
#     if v > 1_000_000:
#         resultado.append("ALTO")
#     else:
#         resultado.append("BAJO")

# Con np.where: una sola línea
import numpy as np
valores = np.array([500_000, 1_500_000, 800_000, 2_000_000], dtype=np.float64)
categorias = np.where(valores > 1_000_000, "ALTO", "BAJO")
print(categorias)   # ['BAJO' 'ALTO' 'BAJO' 'ALTO']
```

Los tres argumentos de `np.where`:
1. **condicion**, un array booleano (o una expresión que produce uno).
2. **valor_si_true**, puede ser un escalar (mismo valor para todos) o un array (valor diferente por posición).
3. **valor_si_false**, igual que el anterior.

### np.where anidado — múltiples tramos

Para lógica con más de dos ramas se anidan llamadas. El `np.where` interior actúa como el `else` del exterior:

```python
dias = np.array([0, 15, 60, 100], dtype=np.int32)

# 0 días → 0 %  |  1-30 → 1 %  |  31-90 → 5 %  |  > 90 → 10 %
tasa = np.where(dias == 0,  0.00,          # si 0 días: 0 %
       np.where(dias <= 30, 0.01,          # si ≤ 30 días: 1 %
       np.where(dias <= 90, 0.05,          # si ≤ 90 días: 5 %
                            0.10)))        # en cualquier otro caso: 10 %

print(tasa)   # [0.   0.01 0.05 0.1 ]
```

La lectura correcta es de arriba hacia abajo: "primero pregunta si `dias == 0`; si no, pregunta si `dias <= 30`; si no, pregunta si `dias <= 90`; si ninguna se cumple, usa `0.10`". Es exactamente la misma lógica de un `if/elif/elif/else`.

### Punto de fallo #7 — olvidar paréntesis en el anidamiento

```python
# INCORRECTO — falta cerrar los paréntesis internos antes de tiempo
tasa = np.where(dias == 0, 0.00,
       np.where(dias <= 30, 0.01,
       np.where(dias <= 90, 0.05, 0.10))  # ← falta un paréntesis de cierre
# SyntaxError: unexpected EOF while parsing

# CORRECTO — un nivel de anidamiento por línea, con su propio cierre
tasa = np.where(
    dias == 0,
    0.00,
    np.where(
        dias <= 30,
        0.01,
        np.where(
            dias <= 90,
            0.05,
            0.10,
        ),
    ),
)
```

Escribir un nivel de anidamiento por línea, en lugar de alinear todo con espacios manuales, hace mucho más fácil contar los paréntesis: cada `np.where(` que abres tiene su `)` de cierre dos líneas más abajo, en la misma columna de indentación.

### Funciones a implementar

#### `clasificar_valores_vectorizado(valores, umbral=1_000_000)`

```python
def clasificar_valores_vectorizado(valores, umbral=1_000_000):
    """
    Clasifica cada valor como "ALTO" o "BAJO" según el umbral.

    Args:
        valores (np.ndarray): Array de valores declarados.
        umbral (float): Valor de corte. Por defecto 1.000.000.

    Returns:
        np.ndarray: Array de cadenas con "ALTO" o "BAJO" por elemento.

    Ejemplo:
        clasificar_valores_vectorizado(
            np.array([500_000, 1_500_000, 800_000, 2_000_000])
        )
        -> array(['BAJO', 'ALTO', 'BAJO', 'ALTO'], dtype='<U4')
    """
```

Implementación:

```python
def clasificar_valores_vectorizado(valores, umbral=1_000_000):
    categoria_alta = "ALTO"
    categoria_baja = "BAJO"
    return np.where(valores > umbral, categoria_alta, categoria_baja)
```

Nombrar `"ALTO"` y `"BAJO"` antes de usarlos no cambia el resultado, pero si en el futuro alguien necesita ajustar el texto de las categorías, sabe exactamente dónde mirar sin tener que interpretar los argumentos de `np.where`.

#### `aplicar_descuento_vectorizado(valores, pagos_voluntarios)`

```python
def aplicar_descuento_vectorizado(valores, pagos_voluntarios):
    """
    Aplica un descuento del 10 % a los valores con pago voluntario.

    Args:
        valores (np.ndarray): Array de valores declarados.
        pagos_voluntarios (np.ndarray): Array booleano, True = pago voluntario.

    Returns:
        np.ndarray: Array con el descuento aplicado donde corresponde.

    Ejemplo:
        aplicar_descuento_vectorizado(
            np.array([1_000_000, 2_000_000, 1_500_000]),
            np.array([True, False, True])
        )
        -> array([ 900000., 2000000., 1350000.])
    """
```

Implementación:

```python
def aplicar_descuento_vectorizado(valores, pagos_voluntarios):
    factor_descuento = 0.90
    valores_con_descuento = valores * factor_descuento
    return np.where(pagos_voluntarios, valores_con_descuento, valores)
```

Aquí el segundo y tercer argumento de `np.where` son arrays, no escalares: `valores_con_descuento` ya tiene calculado el 90 % de cada elemento, y `valores` es el array original sin cambios. NumPy elige elemento a elemento entre los dos según la máscara `pagos_voluntarios`. Calcular `valores_con_descuento` en una línea separada, en vez de escribirlo directamente dentro de `np.where`, evita que la llamada se vuelva difícil de leer de un vistazo.

#### `calcular_sanciones_vectorizadas(valores, dias_mora)`

Esta función aplica la misma lógica de tramos de `calcular_sancion_basica` de sesión 3, pero sobre todos los registros a la vez. La versión de sesión 3 procesaba un registro con `if/elif`; esta procesa todo el array con `np.where` anidado.

```python
def calcular_sanciones_vectorizadas(valores, dias_mora):
    """
    Calcula la sanción básica para cada registro según sus días de mora.

    Tramos:
        0 días        : 0 %
        1 a 30 días   : 1 %
        31 a 90 días  : 5 %
        más de 90 días: 10 %

    Args:
        valores (np.ndarray): Array de valores base.
        dias_mora (np.ndarray): Array de días de mora.

    Returns:
        np.ndarray: Array con la sanción calculada para cada registro.

    Ejemplo:
        calcular_sanciones_vectorizadas(
            np.array([1_000_000, 1_000_000, 1_000_000, 1_000_000]),
            np.array([0, 15, 60, 100])
        )
        -> array([     0.,  10000.,  50000., 100000.])
    """
```

Implementación:

```python
def calcular_sanciones_vectorizadas(valores, dias_mora):
    tasa_sin_mora = 0.00
    tasa_mora_leve = 0.01
    tasa_mora_moderada = 0.05
    tasa_mora_grave = 0.10

    tasa = np.where(
        dias_mora == 0,
        tasa_sin_mora,
        np.where(
            dias_mora <= 30,
            tasa_mora_leve,
            np.where(
                dias_mora <= 90,
                tasa_mora_moderada,
                tasa_mora_grave,
            ),
        ),
    )
    return valores * tasa
```

Nombrar cada tasa antes del `np.where` y escribir un nivel de anidamiento por línea, en vez de alinear todo manualmente con espacios, hace dos cosas: deja claro qué porcentaje corresponde a cada tramo sin tener que descifrarlo entre paréntesis, y si el día de mañana cambia una tasa, basta con editar una línea en lugar de contar columnas para no desalinear el resto.

### Verificar en main.py

Descomenta los tres bloques dentro de `menu_np_where()` y ejecuta `python main.py`, opción `6`.

Salida esperada de sanciones:

```
  Sanciones calculadas:
  900123456 |   0 días | $          0
  800234567 |  30 días | $      8,500
  700345678 |   0 días | $          0
  600456789 |  45 días | $    115,000
  500567890 |  90 días | $     47,500
  400678901 |   0 días | $          0
  300789012 | 120 días | $     45,000
  200890123 |  15 días | $     16,500
```

### Pausa y piensa 💭

> Compara `calcular_sanciones_vectorizadas` con `calcular_sancion_basica` de sesión 3. Escribe al menos dos diferencias concretas: no solo "una usa ciclo y la otra no", sino diferencias en legibilidad, mantenibilidad y qué ocurre si los tramos cambian. ¿Cuál modificarías más fácilmente si las tasas cambian?

### Ejercicios — Sección 6

**Básico:** Modifica `clasificar_valores_vectorizado` para producir tres categorías: `"ALTO"` (> 2M), `"MEDIO"` (> 1M), `"BAJO"`. Usa `np.where` anidado.

**Intermedio:** Implementa `aplicar_intereses_vectorizado(valores, dias_mora, tasa_diaria=0.001)` que calcule `valor * dias * tasa_diaria` para registros con mora y devuelva `0.0` para los demás.

**Avanzado:** Agrega un cuarto tramo a `calcular_sanciones_vectorizadas`: 10 % entre 91 y 180 días, 15 % para más de 180 días.

### Commit de sección

```bash
git add src/numpy_utils.py
git commit -m "sesion-04: sec-6 np.where"
git push
```

---
## Cierre

### Commit final

```bash
git add .
git commit -m "sesion-04: completa — todos los ejercicios"
git push
```

### Lo que aprendiste hoy

En esta sesión transformaste operaciones que en sesiones anteriores requerían ciclos `for` en operaciones directas sobre arrays:

| Sesión 3 (listas + ciclos) | Sesión 4 (NumPy vectorizado) |
|---|---|
| `for v in valores: iva.append(v * 0.19)` | `valores * 0.19` |
| `for v, d in zip(...): if d > 0: filtrados.append(v)` | `valores[dias_mora > 0]` |
| `for v in valores: "ALTO" if v > umbral else "BAJO"` | `np.where(valores > umbral, "ALTO", "BAJO")` |
| `for v, d in zip(...): calcular_sancion(v, d)` | `valores * tasa_vectorizada` |

Al eliminar los ciclos, el código expresa la intención directamente: "multiplica todos los valores por 0.19" en lugar de "para cada valor, multiplícalo y guárdalo en una lista".

### Resumen de puntos de fallo vistos hoy

| # | Situación | Consecuencia | Solución |
|---|---|---|---|
| 1 | `dtype=np.int32` con valores decimales | Decimales truncados silenciosamente | Usar `float64` para valores monetarios |
| 2 | Mezclar strings y números en un array | Todo se convierte a string | Mantener `NITS` como lista separada |
| 3 | `arr[n]` cuando `n >= len(arr)` | `IndexError` | Verificar `arr.shape[0]` antes |
| 4 | Modificar una vista (slice) sin `.copy()` | El array original cambia inesperadamente | Usar `.copy()` al modificar un subarray |
| 5 | `np.sqrt` sobre valores negativos | `nan` sin lanzar excepción | Verificar `np.any(arr < 0)` antes |
| 6 | `and` / `or` entre máscaras booleanas | `ValueError` | Usar `&` y `|` con paréntesis |
| 7 | Paréntesis desbalanceados en `np.where` anidado | `SyntaxError` | Contar que hay tantos `)` como `np.where(` |

### Conexión con la sesión 5

Una **Series** de pandas es internamente un array NumPy con un índice de etiquetas. Un **DataFrame** es una colección de Series alineadas por ese mismo índice. Todas las operaciones de hoy, máscaras, `np.where`, vectorización, funcionan directamente sobre columnas de DataFrames.

```
NumPy array      →   pandas Series     →   pandas DataFrame
[1.5M, 0.85M]        NIT: valor             NIT | Valor | Mora
                      900: 1.5M             900 | 1.5M  | 0
                      800: 0.85M            800 | 0.85M | 30
```

Los mismos patrones de filtrado `arr[mascara]` los usarás con `df[mascara]` en la próxima sesión.

---

## Aparte — Python y el análisis de datos

Python no fue diseñado para ciencia de datos. Nació en **1991** de la mano de Guido van Rossum, un programador holandés que quería un lenguaje fácil de leer y útil para automatizar tareas. Treinta años después, esa decisión de diseño resultó ser exactamente lo que la comunidad de análisis de datos necesitaba.

### La línea del tiempo

```
1991  Python 1.0 — legibilidad como principio de diseño.
       │
1995  Numeric — primeros arrays para cálculo numérico en Python.
       │
2001  SciPy — matemáticas, estadística y optimización científica.
2001  Numarray — alternativa a Numeric para arrays grandes.
       │
2003  Matplotlib — visualización de datos inspirada en MATLAB.
       │
2005  IPython — consola interactiva que cambia cómo se escribe y prueba código.
       │
2006  NumPy 1.0 — Travis Oliphant unifica Numeric y Numarray.
       │
2008  pandas — Wes McKinney crea DataFrames en Python.
       │
2009  scikit-learn — machine learning accesible para todos.
       │
2011  IPython Notebook — código, texto y gráficas en un solo documento.
2014  Jupyter Notebook — nombre definitivo; se vuelve el estándar en academia.
       │
2015  TensorFlow (Google) — deep learning en Python.
2016  Python es el lenguaje más usado en competencias de datos (Kaggle).
       │
2017  PyTorch (Meta) — segunda gran librería de deep learning.
       │
2019  Python es el lenguaje más enseñado en universidades del mundo.
2020  NumPy en Nature. pandas supera los 10 millones de descargas diarias.
       │
2023  Prácticamente todos los modelos de lenguaje grandes se entrenan
       con pipelines escritos en Python.
```

### Por qué Python ganó

Hubo lenguajes más rápidos, más estrictos, más antiguos. R tiene estadística más profunda. MATLAB tenía el mercado científico antes. Julia fue diseñada específicamente para cómputo numérico de alto rendimiento. Ninguno desplazó a Python. Las razones:

**La curva de entrada más baja entre lenguajes de propósito general.** Python no pide declarar tipos, ni entender punteros, ni compilar antes de ejecutar. Para alguien que viene de Excel o SQL, la transición es mucho menos costosa que a Java, C++ o incluso R.

```python
# Código Python válido. Sin plantilla, sin clase, sin compilación.
valores = [1_500_000, 850_000, 2_300_000]
total = sum(valores)
print(f"Total: ${total:,}")
```

**Fue diseñado como lenguaje de integración.** Guido van Rossum llamó a Python un "lenguaje de pegamento": su propósito original era conectar componentes escritos en otros lenguajes. Eso lo hizo natural para envolver librerías de C y Fortran que ya existían en el mundo científico. NumPy, SciPy y pandas envolvieron ese código con una interfaz accesible.

**El notebook como entorno de pensamiento.** Jupyter Notebook cambió cómo se trabaja con datos. En lugar de escribir un programa completo y ejecutarlo, puedes escribir una celda, ver el resultado, ajustar y continuar. Es el ciclo natural del análisis exploratorio, prueba, observa, interpreta, ajusta, y Python fue el primero en tener una herramienta madura para hacerlo.

**Un ecosistema que resuelve problemas reales.** PyPI, el repositorio central de paquetes de Python, tiene hoy más de 500.000 librerías publicadas. Cuando un analista necesita leer un formato de archivo poco común, conectarse a una API específica o aplicar un algoritmo estadístico especializado, la probabilidad de que alguien ya lo haya construido es alta.

**La legibilidad como ventaja de mantenimiento.** Un script de análisis escrito en Python en 2018 sigue siendo legible en 2026. No requiere un entorno especial, no depende de una licencia de software, y otra persona del equipo puede entenderlo sin que quien lo escribió esté disponible. En entornos donde los proyectos duran años y los equipos cambian, ese atributo tiene un valor enorme.

Python resultó ser suficientemente bueno para casi todas las tareas, muy fácil de aprender y el único con un ecosistema que cubría todo el flujo de trabajo: ingestión, limpieza, análisis, modelado, visualización y despliegue. Esa combinación es difícil de superar.

---
