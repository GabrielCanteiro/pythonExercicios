'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''
import random
from time import sleep
print('=========JO KEN PO=========')
'''
#Forma que eu desenvolvi sem consultar a correção
pedra = 0
papel = 1
tesoura = 2
cpu = random.randint(0,2)

jogador = int(input('Suas opções:\n'
                    '[ 0 ] PEDRA\n'
                    '[ 1 ] PAPEL\n'
                    '[ 2 ] TESOURA\n'
                    'Escolha sua Jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

if cpu == pedra and jogador == tesoura:
    print('Computador escolheu Pedra\n'
          'Jogador escolheu Tesoura\n'
          'Computador Venceu!!')
elif cpu == pedra and jogador == papel:
    print('Computador escolheu Pedra\n'
          'Jogador escolheu Papel\n'
          'Jogador Venceu!!')
elif cpu == papel and jogador == tesoura:
    print('Computador escolheu Papel\n'
          'Jogador escolheu Tesoura\n'
          'Jogador Venceu!!')
elif cpu == papel and jogador == pedra:
    print('Computador escolheu Papel\n'
          'Jogador escolheu Pedra\n'
          'Computador Venceu!!')
elif cpu == tesoura and jogador == pedra:
    print('Computador escolheu Tesoura\n'
          'Jogador escolheu Pedra\n'
          'Jogador Venceu!!')
elif cpu == tesoura and jogador == papel:
    print('Computador escolheu Tesoura\n'
          'Jogador escolheu Papel\n'
          'Computador Venceu!!')
elif cpu == jogador:
    print('EMPATE!!\n'
          'OS DOIS ESCOLHERAM A MESMA OPÇÃO{}')

'''
#Forma apos a correção
itens =('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,2)
print('O cumputador escolheu {}'.format(itens[computador]))
print('''Suas opções:
[ 0 ]  PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('=-'*10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-'*10)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador ==2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')