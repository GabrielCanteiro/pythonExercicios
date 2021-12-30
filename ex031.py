'''
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
 Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
d = int(input('Qual a distancia da viagem? '))
preco1 = 0.50 * d
preco2 = 0.45 * d

print('A distancia é de {} Km\nv'.format(d))
if d < 200:
    print('O valor da viagem é de R$ {:.2f}'.format(preco1))
else:
    print('O valor da viagem é de R$ {:.2f}'.format(preco2))