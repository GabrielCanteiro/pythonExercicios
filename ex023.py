#Faça um programa que leia um numero de 0 a 9999 e mostra na tela cada um dos digitos separados.
# Ex: digite um numero: 1834.
# unidades: 4.
# Dezenas: 3.
# Centena: 8.
# milhar: 1
num = int((input('Digite um numero de 0 a 9999: ')))
u = num // 1 % 10
d = num //10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))