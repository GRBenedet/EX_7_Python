#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('qual o seu salario? R$'))

if sal <= 1250:
    aumt = sal + (sal * 15 / 100)
    porc = 15
else:
    aumt = sal + (sal * 10 / 100)
    porc = 10

print('O salario aumentou R${}% e agora é R${:.2f}.'.format(porc , aumt))