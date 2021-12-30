'''
Faça um programa que leia  nome completo de uma pessoa,
mostrando e seguida o primeiro e o ultimo nome separadamente.
ex: Ana Maria de Souza
primeiro = Ana
segundo = Souza
'''
n = str(input('Digite seu nome completo: ')).lower().strip()
nome = n.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))
