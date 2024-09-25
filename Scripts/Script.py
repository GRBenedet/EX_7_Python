#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

alet = randint(0 , 5)

num = int(input('Tente acertar o numero que eu escoli... DICA: ele vai de 1 a 5 -----> '))

if num == alet:
    print('você acertou... parabens!!!')

else:
    print('você errou... haha... ha, eu pensei no numero {} não no {}.'.format(alet , num))