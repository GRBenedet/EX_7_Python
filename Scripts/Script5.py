#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('digite um ano ou digite 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    print('O ano de {} é BISSEXTO.'.format(ano))
else:
    print('O ano de {} não é BISSEXTO.'.format(ano))