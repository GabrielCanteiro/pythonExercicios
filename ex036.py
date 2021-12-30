'''
Exercicio Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o Valor da casa, o Salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mesnal, sabendo que ela nao pode exceder 30% do salário ou então o empréstimo será negado
'''
valor = float(input('Qual o valor da casa que deseja comprar? '))
salario = float(input('Por questões de análises, precio que me diga o seu salário: '))
tempo = int(input('Em quantos anos deseja pagar o imóvel? '))

parcela = tempo * 12
valorParcela = float(valor / parcela)

if valorParcela >= salario - (salario * .70):
    print('Infelizmente não será possível aprovar o emprestimo.')
else:
    print('Parabéns, o empréstimo foi \33[:32mAPROVADO!\33[m')

print('-'*10)

print('30% equivale a R$ {} do seu salário'.format(salario - (salario * .70)))
print('o Valor da parcela está em R${}'.format(valorParcela))
print('O empréstimo será quitado em {} meses'.format(parcela))


