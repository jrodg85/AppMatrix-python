# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 09:56:04 2023

@author: jrodg85
"""

import jrodg85mod1 


# Pedir al usuario la matriz de datos
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f"Ingrese el valor de la posición ({i}, {j}): "))
        fila.append(valor)
    matriz.append(fila)

# Obtener estadísticas por columna
print("\nEstadísticas por columna:")
for i in range(columnas):
    estadisticas = jrodg85mod1.estadistica_por_columna(matriz, i)
    print(f"Columna {i}: Mínimo = {estadisticas[0]}, Máximo = {estadisticas[1]}, Promedio = {estadisticas[2]}")

# Obtener estadísticas por fila
print("\nEstadísticas por fila:")
for i in range(filas):
    estadisticas = jrodg85mod1.estadistica_por_fila(matriz, i)
    print(f"Fila {i}: Mínimo = {estadisticas[0]}, Máximo = {estadisticas[1]}, Promedio = {estadisticas[2]}")

