# -*- coding: utf-8 -*-
"""Samuel.exercicio 10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DF2gxU-5sxWpKpDA_XAG9EE875HsBM7R
"""

cont_gre = 0
cont_g = 0
e = 0
cont_i = 0
perg = 1
while perg == 1:
  gols_gremio = int(input('quantos gols o grêmio fez? '))
  gols_inter = int(input('quantos gols o inter fez? '))
  cont_gre = cont_gre + 1

  if gols_gremio == gols_inter:
        e = e + 1
  elif gols_gremio > gols_inter:
        cont_g += 1
  else:
        cont_i += 1
 
  perg = int(input('você quer um novo jogo? '))
else:
   print('total de {} grenais'.format(cont_gre))
   print('o gremio fez {} vitorias'.format(cont_g))
   print('o inter fez {} vitorias'.format(cont_i))
   print('um total de {} empates'.format(e))
if cont_g == cont_i:
  print('empate')
elif cont_g > cont_i:
  print('gremio venceu mais')
else:
  print('inter venceu mais')