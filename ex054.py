'''
Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
anoatual = date.today().year
cont = 0

for pessoa in range(1,8):
    nasc = int(input('Digite o ano de nascimento da pessoa {}: '.format(pessoa)))
    idade = anoatual - nasc
if idade >= 21:
    print(' {}')