# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 09:56:04 2023

@author: jrodg85
"""
import sys
# import termios
import os
import numpy as np


opcionMenu=""
rows=""
columns=""
matrix=""

def get_integer_input():
    while True:
        try:
            integer_input = int(input("Introduzca un número entero: "))
            return integer_input
        except ValueError:
            print("El valor introducido no es un número entero válido. Por favor, inténtelo de nuevo.")

def get_float_input():
    while True:
        try:
            num = float(input("Ingrese un número: "))
            return num
        except ValueError:
            print("¡Error! Por favor ingrese un número válido.")

def noHayMatriz():
        print("""No hay matriz de estudio.
Procediendo a introducir matriz de estudio.
Una vez introducida la matriz volvera al menu principal.""")
        introduzcaUnaMatriz()
        
def volverAMenuPrincipal():
    print("Presione una tecla para continuar...")
    # wait_for("")
    # borrarPantalla()
    seleccionMenu()

# def borrarPantalla(): # Metodo de borrar pantalla encontrado en https://unipython.com/como-borrar-pantalla-en-python/ Definimos la función estableciendo el nombre que queramos
#     if os.name == "posix":
#         os.system ("clear")
#     elif os.name == "ce" or os.name == "nt" or os.name == "dos":
#         os.system ("cls")

# def wait_for(mess, *keys):## wait for importado de la siguiente url https://es.stackoverflow.com/questions/277815/como-hago-un-presione-enter-para-continuar-en-python-3-linux En spider no funciona correctamente pero en la terminal funciona
#     file_descriptor = sys.stdin.fileno()
#     old = termios.tcgetattr(file_descriptor)
#     new = old[:]
#     try:
#         new[3] &= ~(termios.ICANON | termios.ECHO)
#         termios.tcsetattr(file_descriptor, termios.TCSADRAIN, new)
#         print(mess, end="")
#         while True:
#             letra = sys.stdin.read(1)
#             if not keys or letra in keys:
#                 print()
#                 break
#     finally:
#         termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old)

def introduzcaUnaMatriz():
    global rows
    global columns
    global matrix
    print("Introduzca el numero de filas de la matriz: ")
    rows = get_integer_input()
    print("Introduzca el numero de columnas de la matriz: ")
    columns = get_integer_input()

    matrix = np.empty((rows, columns))

    for i in range(rows):
        for j in range(columns):
            print(f"Ingresa el valor de la fila {i}, columna {j}: ")
            value= get_float_input()
            matrix[i][j] = value
    verMatriz()
    print(matrix)
    print("Presione una tecla para continuar...")
    # wait_for("")
    # borrarPantalla()
    seleccionMenu()
   
def salirDeAppMatrix():
    print("Borrando datos almacenados.")
    global rows
    global columns
    global matrix
    global opcionM
    del (rows,columns,matrix)
    print("Adios.")
    exit()

def verMatriz():
    global matrix
    print("entra en funcion verMatriz")

    print (f""""La matriz de estudio es: 
{matrix}""")
    volverAMenuPrincipal()

def seleccionMenu():
    global opcionMenu
    opcionMenu=input("""Seleccione una opción:
    1 ==> Introduzca una Matriz.
    2 ==> Realizar Estadistica por fila.
    3 ==> Realizar Estadistica por columna.
    4 ==> Ver la matriz.
    5 ==> Salir del programa.
Opcion: """)
    if opcionMenu=="1":
        introduzcaUnaMatriz()
    elif opcionMenu=="2":
        print("pasa por opcionMenu 2")
    elif opcionMenu=="3":
        print("pasa por opcionMenu 3")
    elif opcionMenu=="4":
        print("pasa por opcionMenu 4")
        verMatriz()
    elif opcionMenu=="5":
        salirDeAppMatrix()
    else:
        # borrarPantalla()
        print("Seleccion incorrecta, ha seleccionado '", opcionMenu,"'.")
        seleccionMenu()

# borrarPantalla()
print("Bienvenido a AppMatrix:")
seleccionMenu()
