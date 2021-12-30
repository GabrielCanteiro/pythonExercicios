'''
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá escrever
na tela se o usuário venceu ou perdeu.
'''
import random
import sleep
cpu = random.randint(0, 5)
print('O numero entre 0 e 5 já foi escolhido')
# print(cpu)
user = int(input('Advinhe qual é o numero: '))

if user == cpu:
    print('UAAAU, VOCE VENCEU!!')
else:
    print('EROOOOOOU, voce nao foi capaz de acertar')

