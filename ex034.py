'''
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Qual seu salario? '))
up10 = salario + (salario * .10)
up15 = salario + (salario * .15)

if salario > 1250:
    print('Seu salario teve um aumento de 10% e agora é de R$ {:.2f} !!'.format(up10))
else:
    print('Seu salario teve um aumento de 15% e agora é de R$ {:.2f} !!'.format(up15))