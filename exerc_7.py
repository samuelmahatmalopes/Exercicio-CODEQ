# -*- coding: utf-8 -*-
"""exerc.7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F8Fo3qh_W60WckOMpY0Rtmg-qIIMF0HW
"""

idade = int(input())

anos = int(idade / 365)


saldo = idade - (anos * 365)

meses = int(saldo / 30)



dias = saldo - meses * 30

print(anos, 'anos(s)')

print(meses, 'meses(es)')

print(anos, 'dias(s)')