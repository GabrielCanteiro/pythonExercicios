'''
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
print('===========BEM VINDO A LOJA===============')
total = float(input('Qual foi o valor total das suas compras? R$ '))

print('===========Forma de Pagamento===============')
pagamento = int(input('''Qual será a forma de pagamento? Temos condições especiais para cada uma delas!!
                      [ 1 ] à vista dinheiro/cheque: 10% de desconto
                      [ 2 ] à vista no cartão: 5% de desconto
                      [ 3 ] em até 2x no cartão: preço formal
                      [ 4 ] 3x ou mais no cartão: 20% de juros
                      Eai, qual será (1,2,3 ou 4)? '''))

if pagamento == 1:
    print('Vocé teve um desconto de 10%. O valor a ser pago é de R${:.2f}'.format(total - (total * .10)))
elif pagamento == 2:
    print('Você teve um desconto de 5%. O valor a ser pago é de R${:.2f}'.format(total-(total *.05)))
elif pagamento == 3:
    print('O valor a ser pago é de R${:.2f}'.format(total))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = total+(total*.2)
    print('Dessa forma serão {}x de R${:.2f} com juros.'.format(parcelas,juros/parcelas))
    print('Sua compra de R${:.2f} irá custar R${:.2f} no final'.format(total, juros))
else:
    print('Opção invalida, tente novamente')