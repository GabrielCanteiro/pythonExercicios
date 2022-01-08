'''
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
import random
from time import sleep
cpu = random.randint(0, 10)
nome = input('Digite seu nome para começarmos: ').strip().title()
sleep(0.5)
print('Bem vindo {}, Eu sou seu computador'
      ' e já escolhi um numero de 0 a 10.'.format(nome))
sleep(0.5)
#print(cpu)
user = int(input('Advinhe qual é o numero: '))
cont = 1
while cpu != user:
    cont += 1
    if cpu > user:
        user = int(input('um pouco mais... Tente novamente: '))
    else:
        user = int(input('Um pouco menos... Tente novamente: '))
print('''Você precisou de {} tentativas, E VENCEU!!'''.format(cont))

'''if user == cpu:
    print('UAAAU, VOCE VENCEU!!')
else:
    print('EROOOOOOU, voce nao foi capaz de acertar')'''

