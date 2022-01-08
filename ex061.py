'''
Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
print('=========== 10 TERMOS DE UM PA ============')

termo = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
decimo = termo + (10-1) * raz
for c in range(termo,decimo + raz,raz):
    print('{} ➡ '.format(c),end='')
print('Acabou')