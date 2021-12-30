'''
Exercício Python 30:
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

n = int(input('Digite um numero: '))
par = n % 2

if par == 0:
    print('par')
else:
    print('impar')
