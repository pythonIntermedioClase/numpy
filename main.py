# main.py
# Proyecto: Análisis con NumPy - DIAN 2026
# Sesión 4: arrays, vectorización, ufuncs, máscaras booleanas y np.where
#
# Ejecutar con: python main.py
#
# Instrucciones:
#   1. Completa cada función en src/numpy_utils.py.
#   2. Descomenta el bloque correspondiente en este archivo.
#   3. Ejecuta python main.py y verifica la salida.
#   4. git add, commit y push al terminar cada sección.

import numpy as np

from src.numpy_utils import VALORES_DECLARADOS, DIAS_MORA, NITS

from src.numpy_utils import describir_array
from src.numpy_utils import crear_array_declaraciones
from src.numpy_utils import comparar_lista_vs_array
from src.numpy_utils import filtrar_valores_en_rango

from src.numpy_utils import obtener_rango
from src.numpy_utils import obtener_ultimos
from src.numpy_utils import invertir_array

from src.numpy_utils import calcular_iva_todos
from src.numpy_utils import calcular_valor_con_iva
from src.numpy_utils import redondear_a_miles

from src.numpy_utils import calcular_variacion_absoluta
from src.numpy_utils import normalizar_valores
from src.numpy_utils import aplicar_raiz_cuadrada

from src.numpy_utils import contar_con_ciclo
from src.numpy_utils import sumar_con_ciclo
from src.numpy_utils import obtener_mascara_mora
from src.numpy_utils import filtrar_valores_con_mora
from src.numpy_utils import contar_sobre_umbral

from src.numpy_utils import clasificar_valores_vectorizado
from src.numpy_utils import aplicar_descuento_vectorizado
from src.numpy_utils import calcular_sanciones_vectorizadas


# ---------------------------------------------------------------------------
# Menú
# ---------------------------------------------------------------------------

def menu_arrays_y_tipos():
    """Sección 1: arrays y tipos de datos."""
    print("\n--- Arrays y tipos de datos ---")

    # TODO: descomenta cuando hayas implementado describir_array
    # print("\n  VALORES_DECLARADOS:")
    # describir_array(VALORES_DECLARADOS)
    # print("\n  DIAS_MORA:")
    # describir_array(DIAS_MORA)

    # TODO: descomenta cuando hayas implementado crear_array_declaraciones
    # lista = [1_200_000, 750_000, 3_100_000]
    # arr = crear_array_declaraciones(lista)
    # print(f"\n  Array creado desde lista: {arr}")
    # print(f"  Tipo: {arr.dtype}")

    # TODO: descomenta cuando hayas implementado comparar_lista_vs_array
    # valores_lista = [1_500_000, 850_000, 2_300_000, 950_000]
    # comparar_lista_vs_array(valores_lista)

    # TODO: descomenta cuando hayas implementado filtrar_valores_en_rango
    # valores_lista = [1_500_000, 850_000, 2_300_000, 950_000, 0, 3_200_000]
    # en_rango = filtrar_valores_en_rango(valores_lista, 500_000, 2_000_000)
    # print(f"\n  Valores entre 500.000 y 2.000.000: {en_rango}")

    print("\n  (función pendiente de implementar)")


def menu_indexacion_slicing():
    """Sección 2: indexación y slicing."""
    print("\n--- Indexación y slicing ---")

    # TODO: descomenta cuando hayas implementado obtener_rango
    # rango = obtener_rango(VALORES_DECLARADOS, 2, 5)
    # print(f"\n  Posiciones 2 a 4: {rango}")

    # TODO: descomenta cuando hayas implementado obtener_ultimos
    # ultimos = obtener_ultimos(VALORES_DECLARADOS, 3)
    # print(f"\n  Últimos 3 valores: {ultimos}")

    # TODO: descomenta cuando hayas implementado invertir_array
    # invertido = invertir_array(VALORES_DECLARADOS)
    # print(f"\n  Array invertido: {invertido}")

    print("\n  (función pendiente de implementar)")


def menu_vectorizacion():
    """Sección 3: vectorización."""
    print("\n--- Vectorización ---")

    # TODO: descomenta cuando hayas implementado calcular_iva_todos
    # iva = calcular_iva_todos(VALORES_DECLARADOS)
    # print("\n  IVA por declaración:")
    # for i, (nit, valor, monto_iva) in enumerate(
    #         zip(NITS, VALORES_DECLARADOS, iva)):
    #     print(f"  {nit} | ${valor:>12,.0f} | IVA: ${monto_iva:>10,.0f}")

    # TODO: descomenta cuando hayas implementado calcular_valor_con_iva
    # con_iva = calcular_valor_con_iva(VALORES_DECLARADOS)
    # print(f"\n  Primeros 3 valores con IVA: {con_iva[:3]}")

    # TODO: descomenta cuando hayas implementado redondear_a_miles
    # redondeados = redondear_a_miles(VALORES_DECLARADOS * 1.19)
    # print(f"\n  Valores con IVA redondeados a miles: {redondeados}")

    print("\n  (función pendiente de implementar)")


def menu_ufuncs():
    """Sección 4: funciones universales."""
    print("\n--- Funciones universales ---")

    # TODO: descomenta cuando hayas implementado calcular_variacion_absoluta
    # valores_anterior = np.array([
    #     1_200_000, 900_000, 0, 2_100_000,
    #     800_000, 3_000_000, 500_000, 1_000_000,
    # ], dtype=np.float64)
    # variacion = calcular_variacion_absoluta(VALORES_DECLARADOS, valores_anterior)
    # print("\n  Variación absoluta respecto al período anterior:")
    # for nit, var in zip(NITS, variacion):
    #     print(f"  {nit} | ${var:>10,.0f}")

    # TODO: descomenta cuando hayas implementado normalizar_valores
    # normalizados = normalizar_valores(VALORES_DECLARADOS)
    # print("\n  Valores normalizados [0-1]:")
    # for nit, norm in zip(NITS, normalizados):
    #     print(f"  {nit} | {norm:.3f}")

    # TODO: descomenta cuando hayas implementado aplicar_raiz_cuadrada
    # raices = aplicar_raiz_cuadrada(VALORES_DECLARADOS)
    # print(f"\n  Raíz cuadrada (primeros 3): {raices[:3]}")

    print("\n  (función pendiente de implementar)")


def menu_boolean_arrays():
    """Sección 5: arrays booleanos."""
    print("\n--- Arrays booleanos ---")

    # TODO: descomenta cuando hayas implementado contar_con_ciclo y sumar_con_ciclo
    # valores_lista = [1_500_000, 850_000, 0, 2_300_000,
    #                  950_000, 3_200_000, 450_000, 1_100_000]
    # umbral = 1_000_000
    # cantidad = contar_con_ciclo(valores_lista, umbral)
    # total = sumar_con_ciclo(valores_lista)
    # print(f"\n  contar_con_ciclo:           {cantidad}")
    # print(f"  np.sum(arr > umbral):       {contar_sobre_umbral(VALORES_DECLARADOS, umbral)}")
    # print(f"\n  sumar_con_ciclo:            {total}")
    # print(f"  np.sum(arr):                {np.sum(VALORES_DECLARADOS)}")

    # TODO: descomenta cuando hayas implementado obtener_mascara_mora
    # mascara = obtener_mascara_mora(DIAS_MORA)
    # print(f"\n  Máscara de mora: {mascara}")
    # print(f"  Registros en mora: {np.sum(mascara)} de {len(mascara)}")

    # TODO: descomenta cuando hayas implementado filtrar_valores_con_mora
    # en_mora = filtrar_valores_con_mora(VALORES_DECLARADOS, DIAS_MORA)
    # print(f"\n  Valores declarados con mora:")
    # for valor in en_mora:
    #     print(f"    ${valor:,.0f}")
    # print(f"  Total en riesgo: ${en_mora.sum():,.0f}")

    # TODO: descomenta cuando hayas implementado contar_sobre_umbral
    # umbral = 1_000_000
    # cantidad = contar_sobre_umbral(VALORES_DECLARADOS, umbral)
    # print(f"\n  Registros sobre ${umbral:,}: {cantidad}")

    print("\n  (función pendiente de implementar)")


def menu_np_where():
    """Sección 6: np.where."""
    print("\n--- np.where ---")

    # TODO: descomenta cuando hayas implementado clasificar_valores_vectorizado
    # categorias = clasificar_valores_vectorizado(VALORES_DECLARADOS)
    # print("\n  Clasificación de declaraciones:")
    # for nit, valor, cat in zip(NITS, VALORES_DECLARADOS, categorias):
    #     print(f"  {nit} | ${valor:>12,.0f} | {cat}")

    # TODO: descomenta cuando hayas implementado aplicar_descuento_vectorizado
    # pagos_voluntarios = np.array([True, False, False, True,
    #                               False, True, False, False])
    # con_descuento = aplicar_descuento_vectorizado(
    #     VALORES_DECLARADOS, pagos_voluntarios)
    # print("\n  Valores con descuento voluntario:")
    # for nit, original, final, voluntario in zip(
    #         NITS, VALORES_DECLARADOS, con_descuento, pagos_voluntarios):
    #     marca = " ← descuento 10%" if voluntario else ""
    #     print(f"  {nit} | ${original:>12,.0f} → ${final:>12,.0f}{marca}")

    # TODO: descomenta cuando hayas implementado calcular_sanciones_vectorizadas
    # sanciones = calcular_sanciones_vectorizadas(VALORES_DECLARADOS, DIAS_MORA)
    # print("\n  Sanciones calculadas:")
    # for nit, valor, dias, sancion in zip(
    #         NITS, VALORES_DECLARADOS, DIAS_MORA, sanciones):
    #     print(f"  {nit} | {dias:>3} días | ${sancion:>10,.0f}")

    print("\n  (función pendiente de implementar)")


# ---------------------------------------------------------------------------
# Menú principal
# ---------------------------------------------------------------------------

def mostrar_menu():
    print("\n" + "=" * 50)
    print("  Sesión 4 — NumPy para análisis tributario")
    print("=" * 50)
    print("  1. Arrays y tipos de datos")
    print("  2. Indexación y slicing")
    print("  3. Vectorización")
    print("  4. Funciones universales (ufuncs)")
    print("  5. Arrays booleanos")
    print("  6. np.where")
    print("  0. Salir")
    print("-" * 50)


OPCIONES = {
    "1": ("Arrays y tipos de datos",     menu_arrays_y_tipos),
    "2": ("Indexación y slicing",         menu_indexacion_slicing),
    "3": ("Vectorización",               menu_vectorizacion),
    "4": ("Funciones universales",       menu_ufuncs),
    "5": ("Arrays booleanos",            menu_boolean_arrays),
    "6": ("np.where",                    menu_np_where),
    "0": ("Salir",                       None),
}


def main():
    """Punto de entrada. Ejecuta el menú interactivo con variable bandera."""
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()
        if opcion in OPCIONES:
            nombre, funcion = OPCIONES[opcion]
            if funcion is None:
                continuar = False
                print("\nHasta la proxima.\n")
            else:
                funcion()
                input("\n  Presiona Enter para volver al menu...")
        else:
            print(f"\n  Opcion '{opcion}' no reconocida.")


if __name__ == "__main__":
    main()
