"""
numpy_utils_solucion.py - Solucionario de la sesión 4 (NumPy).

Versión de numpy_utils.py con todas las funciones diligenciadas, tal como
quedan descritas en sesion_04.md. Es material del instructor para
verificación y apoyo, no se distribuye en el repositorio plantilla.
"""

import numpy as np


# ---------------------------------------------------------------------------
# Datos de práctica
# ---------------------------------------------------------------------------

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


# ===========================================================================
# SECCIÓN 1: ARRAYS Y TIPOS DE DATOS
# ===========================================================================

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
    print(f"  Forma   : {arr.shape}")
    print(f"  Tipo    : {arr.dtype}")
    print(f"  Mínimo  : {arr.min()}")
    print(f"  Máximo  : {arr.max()}")


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
    return np.array(valores_lista, dtype=np.float64)


def comparar_lista_vs_array(valores_lista):
    """
    Imprime la diferencia entre operar sobre una lista y sobre un array.

    Muestra que con una lista Python hay que usar un ciclo for para
    multiplicar cada elemento, mientras que con un array basta con
    escribir arr * 0.19.

    Es un procedimiento: no retorna ningún valor.

    Args:
        valores_lista (list): Lista de números de referencia.

    Ejemplo de salida:
        Lista (requiere ciclo for):
          [285000.0, 161500.0, ..., 209000.0]
        Array (operación directa):
          [285000.   161500.   ...  209000.  ]
    """
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


def filtrar_valores_en_rango(valores_lista, minimo, maximo):
    """
    Retorna una lista nueva con los valores que están entre minimo y maximo.

    Recorre la lista con un ciclo for y usa un condicional para decidir
    si cada valor entra en el rango. Esto retoma el ejercicio de listas
    que no se cubrió en la sesión 3.

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
    filtrados = []
    for valor in valores_lista:
        if minimo <= valor <= maximo:
            filtrados.append(valor)
    return filtrados


# ===========================================================================
# SECCIÓN 2: INDEXACIÓN Y SLICING
# ===========================================================================

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
    return arr[inicio:fin]


def obtener_ultimos(arr, n):
    """
    Retorna los últimos n elementos del array.

    Args:
        arr (np.ndarray): Array de NumPy.
        n (int): Número de elementos a retornar desde el final.

    Returns:
        np.ndarray: Subarray con los últimos n elementos.

    Ejemplo:
        obtener_ultimos(VALORES_DECLARADOS, 3)
        -> array([ 450000., 1100000.])  (últimos 3 elementos)
    """
    return arr[-n:]


def invertir_array(arr):
    """
    Retorna una copia del array con los elementos en orden invertido.

    Args:
        arr (np.ndarray): Array de NumPy.

    Returns:
        np.ndarray: Array con elementos en orden invertido.

    Ejemplo:
        invertir_array(np.array([1, 2, 3, 4]))
        -> array([4, 3, 2, 1])
    """
    return arr[::-1]


# ===========================================================================
# SECCIÓN 3: VECTORIZACIÓN
# ===========================================================================

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
    return valores * tasa


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
    factor_con_iva = 1 + tasa
    return valores * factor_con_iva


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
    valor_en_miles = arr / 1000
    miles_redondeados = np.round(valor_en_miles)
    return miles_redondeados * 1000


# ===========================================================================
# SECCIÓN 4: FUNCIONES UNIVERSALES (UFUNCS)
# ===========================================================================

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
    return np.abs(valores_actuales - valores_anteriores)


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
    minimo = arr.min()
    maximo = arr.max()
    return (arr - minimo) / (maximo - minimo)


def aplicar_raiz_cuadrada(arr):
    """
    Calcula la raíz cuadrada de cada elemento del array.

    Útil para transformar distribuciones sesgadas antes de comparar valores.

    Args:
        arr (np.ndarray): Array de valores no negativos.

    Returns:
        np.ndarray: Array con la raíz cuadrada de cada elemento.

    Ejemplo:
        aplicar_raiz_cuadrada(np.array([0, 100_000, 400_000, 900_000]))
        -> array([  0.      , 316.22...,  632.45...,  948.68...])
    """
    return np.sqrt(arr)


# ===========================================================================
# SECCIÓN 5: ARRAYS BOOLEANOS
# ===========================================================================

def contar_con_ciclo(lista, umbral):
    """
    Cuenta cuántos elementos de la lista superan el umbral, usando un ciclo for.

    Función de práctica, sin NumPy. Es el patrón del contador, antes de
    ver su versión vectorizada en contar_sobre_umbral.

    Args:
        lista (list): Lista de valores numéricos.
        umbral (float): Valor de referencia.

    Returns:
        int: Número de elementos mayores que umbral.

    Ejemplo:
        contar_con_ciclo([1_500_000, 850_000, 0, 2_300_000], 1_000_000)
        -> 2
    """
    contador = 0
    for valor in lista:
        if valor > umbral:
            contador += 1
    return contador


def sumar_con_ciclo(lista):
    """
    Suma todos los elementos de la lista, usando un ciclo for.

    Función de práctica, sin NumPy. Es el patrón del acumulador, antes de
    ver su versión vectorizada con np.sum.

    Args:
        lista (list): Lista de valores numéricos.

    Returns:
        float: Suma de todos los elementos.

    Ejemplo:
        sumar_con_ciclo([1_500_000, 850_000, 2_300_000])
        -> 4650000
    """
    total = 0
    for valor in lista:
        total += valor
    return total


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
    return dias_mora > 0


def filtrar_valores_con_mora(valores, dias_mora):
    """
    Retorna los valores declarados de los registros que tienen mora.

    Usa una máscara booleana para seleccionar solo los elementos
    donde hay mora (dias_mora > 0).

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
    mascara = dias_mora > 0
    return valores[mascara]


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
    mascara = arr > umbral
    cantidad = np.sum(mascara)
    return int(cantidad)


# ===========================================================================
# SECCIÓN 6: NP.WHERE
# ===========================================================================

def clasificar_valores_vectorizado(valores, umbral=1_000_000):
    """
    Clasifica cada valor como "ALTO" o "BAJO" según el umbral.

    En sesión 3 hacíamos esto con if/elif. Con np.where, la clasificación
    opera sobre todos los elementos sin escribir un ciclo.

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
    categoria_alta = "ALTO"
    categoria_baja = "BAJO"
    return np.where(valores > umbral, categoria_alta, categoria_baja)


def aplicar_descuento_vectorizado(valores, pagos_voluntarios):
    """
    Aplica un descuento del 10 % a los valores con pago voluntario.

    Versión vectorizada de aplicar_descuento de sesión 3.

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
    factor_descuento = 0.90
    valores_con_descuento = valores * factor_descuento
    return np.where(pagos_voluntarios, valores_con_descuento, valores)


def calcular_sanciones_vectorizadas(valores, dias_mora):
    """
    Calcula la sanción básica para cada registro según sus días de mora.

    Aplica la misma lógica de tramos de calcular_sancion_basica de sesión 3,
    pero sobre todos los registros simultáneamente usando np.where anidados.

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
