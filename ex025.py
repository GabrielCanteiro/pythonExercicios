'''
Crie um programa que leia o nome de uma pessoa e
diga se ela tem "Silva" no nome
'''
nome = str(input('Digite seu nome Completo: ')).strip()
nome2 = 'silva'
print('Esse nome Contem "SILVA"?: {}'.format('silva' in nome.lower()))