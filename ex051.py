'''
Exercício Python 051: Desenvolva um programa que leia o primeiro termo
e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
print('=========== 10 TERMOS DE UM PA ============')

termo = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
decimo = termo + (10-1) * raz
for c in range(termo,decimo + raz,raz):
    print('{} ➡ '.format(c),end='')
print('Acabou')