#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = int(input('defina a primeira reta: '))
b = int(input('defina a segunda reta: '))
c = int(input('defina a terceira reta: '))

if a + b > c and b + c > a and a + c > b:
    tf = 'pode'

else:
    tf = 'não pode'

print('as retas {}, {} e {} {} formar um triangulo.'.format(a , b , c , tf))
