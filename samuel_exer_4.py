# -*- coding: utf-8 -*-
"""Samuel.Exer.4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b13xGKZwc80JtuFfpeNKsYrIgA0Ga2cf
"""

a = float(input("Digite um valor para o ponto A: "))
b = float(input("Digite um valor para o ponto B: "))
c = float(input("Digite um valor para o ponto C: "))
area_triang = a * c
area_triang = round(float(area_triang), 3)
area_circ = 3.14159 * c**2
area_circ = round(float(area_circ), 3)
area_trap = (a+b)*c/2
area_trap = round(float(area_trap), 3)
area_quad = b**2
area_quad = round(float(area_quad), 3)
area_retang = a*b
area_retang = round(float(area_retang), 3)
print(f'TRIÂNGULO: {area_triang}')
print(f'CÍRCULO: {area_circ}')
print(f'TRAPÉZIO: {area_trap}')
print(f'QUADRADO: {area_quad}')
print(f'RETÂNGULO: {area_retang}')