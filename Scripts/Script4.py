#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('quantos quilometros vai ser sua viagem? '))

if dist < 200:
    print('a sua viagem de {}, vai custar R$0,50 por km, ficando um total de R${:.2f}.'.format(dist , dist * .5))

else:
    print('a sua viagem de {}, vai custar R$0,45 por km, ficando um total de R${:.2f}.'.format(dist , dist * .45))