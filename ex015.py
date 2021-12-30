#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$60 por dia e R$0,15 por Km rodado.
dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram pecorridos? '))
precoDia = 60*dia
precoKm = 0.15*km
print('='*20)
print('Quanitade de dias utilizados: {}. Totalizando R$ {:.2f}'.format(dia,precoDia))
print('Quanitade de Km percorridos: {}. Totalizando R$ {:.2f}'.format(km,precoKm))
print('Total a ser pago: R$ {:.2f}'.format((precoDia)+precoKm))
print('='*20)