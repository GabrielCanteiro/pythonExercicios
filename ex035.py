'''Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.'''
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and b + c > a and c + a > b:
    print('Dessa forma é possivel formar um triangulo')
else:
    print('Asssim não é possivel formar um triangulo')