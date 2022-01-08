'''
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
from math import factorial
num = int(input('''Digite um número para calcular o seu fatorial.
Qual é o numero? '''))
fat = factorial(num)
print('Calculando {}! ='.format(num),end=' ')
while num > 1:
    print(num, end=' x ',)
    num -= 1
print('{} = {}'.format(num,fat),end='')
