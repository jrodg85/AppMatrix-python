# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 08:32:13 2023

@author: jrodg85
"""

def estadistica_por_columna(matriz, columna=None):
    if columna is not None:
        columna_datos = [fila[columna] for fila in matriz]
        minimo = min(columna_datos)
        maximo = max(columna_datos)
        promedio = sum(columna_datos) / len(columna_datos)
        return minimo, maximo, promedio
    else:
        estadisticas = []
        for i in range(len(matriz[0])):
            columna_datos = [fila[i] for fila in matriz]
            minimo = min(columna_datos)
            maximo = max(columna_datos)
            promedio = sum(columna_datos) / len(columna_datos)
            estadisticas.append((minimo, maximo, promedio))
        return estadisticas


def estadistica_por_fila(matriz, fila=None):
    if fila is not None:
        fila_datos = matriz[fila]
        minimo = min(fila_datos)
        maximo = max(fila_datos)
        promedio = sum(fila_datos) / len(fila_datos)
        return minimo, maximo, promedio
    else:
        estadisticas = []
        for fila in matriz:
            minimo = min(fila)
            maximo = max(fila)
            promedio = sum(fila) / len(fila)
            estadisticas.append((minimo, maximo, promedio))
        return estadisticas
