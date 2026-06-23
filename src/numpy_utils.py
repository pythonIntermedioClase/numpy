"""
numpy_utils.py - Funciones NumPy del proyecto de análisis de declaraciones.

Completa cada función siguiendo las instrucciones en los comentarios TODO.
Cuando termines una función, ve a main.py, descomenta el bloque
correspondiente y ejecuta python main.py para verificar tu resultado.

Autora/Autor: [Tu nombre]
Fecha: [Fecha de la sesión]
"""

import numpy as np


# ---------------------------------------------------------------------------
# Datos de práctica
#
# A diferencia de las sesiones anteriores, los datos son arrays de NumPy,
# no listas de Python. Esto permite operar sobre todos los elementos
# simultáneamente sin escribir ciclos explícitos.
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
    # TODO: imprime forma con arr.shape, tipo con arr.dtype,
    #       mínimo con arr.min() y máximo con arr.max()
    pass


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
    # TODO: usa np.array con el parámetro dtype=np.float64
    pass


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
    # TODO:
    # 1. Calcula el IVA con ciclo for sobre valores_lista y guarda en iva_lista
    # 2. Convierte valores_lista a array con np.array
    # 3. Calcula el IVA multiplicando el array por 0.19 y guarda en iva_array
    # 4. Imprime ambos resultados con etiquetas
    pass


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
    # TODO:
    # 1. Crea una lista vacía para acumular los valores filtrados
    # 2. Recorre valores_lista con un ciclo for
    # 3. Si minimo <= valor <= maximo, agrégalo con .append()
    # 4. Retorna la lista acumulada
    pass


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
    # TODO: usa slicing con arr[inicio:fin]
    pass


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
    # TODO: usa indexación negativa arr[-n:]
    pass


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
    # TODO: usa slicing con paso -1: arr[::-1]
    pass


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
    # TODO: retorna valores * tasa (una sola operación, sin ciclo)
    pass


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
    # TODO:
    # 1. Guarda 1 + tasa en una variable factor_con_iva
    # 2. Retorna valores * factor_con_iva
    pass


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
    # TODO:
    # 1. Divide arr entre 1000 y guarda en valor_en_miles
    # 2. Aplica np.round a valor_en_miles y guarda en miles_redondeados
    # 3. Retorna miles_redondeados * 1000
    pass


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
    # TODO: usa np.abs(valores_actuales - valores_anteriores)
    pass


def normalizar_valores(arr):
    """
    Escala los valores al rango [0, 1] usando normalización min-max.

    La fórmula es: (valor - mínimo) / (máximo - mínimo).
    Un valor de 0.0 corresponde al mínimo y 1.0 al máximo.

    Args:
        arr (np.ndarray): Array de valores numéricos. No debe tener todos
                          los elementos iguales (divisón por cero).

    Returns:
        np.ndarray: Array con valores normalizados entre 0 y 1.

    Ejemplo:
        normalizar_valores(np.array([0, 1_000_000, 2_000_000]))
        -> array([0. , 0.5, 1. ])
    """
    # TODO: calcula minimo = arr.min(), maximo = arr.max()
    #       retorna (arr - minimo) / (maximo - minimo)
    pass


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
    # TODO: usa np.sqrt(arr)
    pass


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
    # TODO:
    # 1. Crea contador = 0, antes del ciclo
    # 2. Recorre lista con un ciclo for
    # 3. Si valor > umbral, suma 1 a contador
    # 4. Retorna contador
    pass


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
    # TODO:
    # 1. Crea total = 0, antes del ciclo
    # 2. Recorre lista con un ciclo for
    # 3. Suma cada valor a total
    # 4. Retorna total
    pass


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
    # TODO: retorna dias_mora > 0
    pass


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
    # TODO:
    # 1. Crea la máscara: mascara = dias_mora > 0
    # 2. Retorna valores[mascara]
    pass


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
    # TODO:
    # 1. Crea la máscara: mascara = arr > umbral
    # 2. Cuenta los True con cantidad = np.sum(mascara)
    # 3. Retorna int(cantidad)
    pass


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
    # TODO:
    # 1. Guarda "ALTO" en categoria_alta y "BAJO" en categoria_baja
    # 2. Retorna np.where(valores > umbral, categoria_alta, categoria_baja)
    pass


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
    # TODO:
    # 1. Guarda 0.90 en factor_descuento
    # 2. Calcula valores_con_descuento = valores * factor_descuento
    # 3. Retorna np.where(pagos_voluntarios, valores_con_descuento, valores)
    pass


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
    # TODO:
    # 1. Guarda cada tasa en una variable con nombre:
    #    tasa_sin_mora = 0.00
    #    tasa_mora_leve = 0.01
    #    tasa_mora_moderada = 0.05
    #    tasa_mora_grave = 0.10
    # 2. Anida np.where para los cuatro tramos, uno por línea:
    #    tasa = np.where(
    #        dias_mora == 0,
    #        tasa_sin_mora,
    #        np.where(
    #            dias_mora <= 30,
    #            tasa_mora_leve,
    #            np.where(
    #                dias_mora <= 90,
    #                tasa_mora_moderada,
    #                tasa_mora_grave,
    #            ),
    #        ),
    #    )
    # 3. Retorna valores * tasa
    pass
