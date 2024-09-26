#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
menor = a

if a < b and a < c:
    menor = a

if b < a and b < c:
    menor = b

maior = c

if a > b and a > c:
    maior = a

if b > a and b > c:
    maior = b
    
menor = c

print('O menor valor é {}. \nO maior valor é {}.'.format(menor , maior))