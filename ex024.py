'''
Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "Santo"
'''

cidade = input('Digite o nome de uma cidade:').strip()
print(cidade[0:5].upper() == 'SANTO')
