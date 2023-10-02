'''
Autor: Alexis Cano
Fecha 2 Octubre
Descripcion: Iniciando con Python

Lab:2.6.1.10
'''

import math

x = float(input("Ingresa el valor para x: "))

# Calcula el valor de y usando la expresión dada
y = 1.0/(x + 1.0/ (x + 1.0 /(x + 1.0 /x)))

print("y =", y)
