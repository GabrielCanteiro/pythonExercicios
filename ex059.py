'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
num1 = int(input('informe o primeiro número: '))
num2 = int(input('informe o segundo número: '))
soma = num1 + num2
mult = num1 * num2
option = 0
while option != 5:
    option = int(input('''o que você deseja fazer com os numeros informados?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
>>>>>>>>> Qual a sua opção? '''))
    if option == 1:
        print('A soma dos numeros {} e {} é {}'.format(num1,num2,num1+num2))
        print('=-='*10)
        sleep(2)
    if option == 2:
        print('A multiplicação entre {} e {} é {}'.format(num1,num2,num1*num2))
        print('=-='*10)
        sleep(2)
    if option == 3:
        if num1 > num2:
            print('entre {} e {}, {} é maior'.format(num1,num2,num1))
        else:
            print('entre {} e {}, {} é maior'.format(num1,num2,num2))
        print('=-='*10)
        sleep(2)
    if option == 4:
        print('Tudo bem, informe os novos numeros abaixo.')
        num1 = int(input('informe o primeiro número: '))
        num2 = int(input('informe o segundo número: '))
        print('=-=' * 10)
        sleep(2)
sleep(2)
print('Processo finalizado, espero que tenha se divertido ;)')
