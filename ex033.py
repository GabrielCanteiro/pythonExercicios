'''
Faça um porgrama que leia tres numeros e mostre qual é o maior e qual é o menor
'''
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

#Verificando o Menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3< n2:
    menor = n3

#Verificando o Maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O menor numero foi {}'.format(menor))
print('O maior numero foi {}'.format(maior))
