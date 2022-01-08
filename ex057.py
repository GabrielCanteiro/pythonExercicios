'''
Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Informe o sexo: [M/F] ')).lower()[0].strip()

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Informe o sexo novamente: [M/F] '))
print('Sexo registrado com sucesso!')


