'''
Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
 A multa vai custar R$7,00 por cada Km acima do limite.
'''

radar = int(input('Qual a velocidade do veiculo? '))
multa = (radar - 80) * 7.00

if radar > 80:
    print('Rodou irmao, multinha de R$ {:.2f} para o senhor.'.format(multa))
else:
    print('Passou de boa, sem prjuizo pra você')
