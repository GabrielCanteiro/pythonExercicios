'''
Exercício Python 038: Escreva um programa que leia dois numeros inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''
print('¨-¨'*15)
print('Vamos comparar para ver qual é o maior!')
print('¨-¨'*15)

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O primeiro valor({}) é maior'.format(n1))
elif n2 > n1:
    print('O segundo valor({}) é maior'.format(n2))
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')
