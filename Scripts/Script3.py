#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('digite um numero: '))

if num % 2 == 0:
    print('o numero {} é PAR.'.format(num))

else:
    print('O numoro {} é IMPAR.'.format(num))