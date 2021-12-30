'''
Exercicio Python 037: Escreva um porgram que leia um numero inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
'''
print('==-=-=-=-=-=-=-=-CONVERSOR=-=-=-=-=-=-=-=-=-=-=')
num = int(input('Digite o numero que deseja converter: '))
print('''Escolha qual será a base de conversão:
[ 1 ] binário
[ 2 ]para octal
[ 3 ]para hexadecimal''')
opcao = int(input('Esolha a sua opção: '))

if opcao == 1:
    print('O numero {} em Binário será: {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('O numero {} em Octal será: {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('O numero {} em Hexadecimal será: {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')