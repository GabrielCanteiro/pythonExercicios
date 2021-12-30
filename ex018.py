#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente desse ângulo.
import math
x = int(input('Qual o angulo?: '))
print('O seno: {:.2f}'.format(math.sin(math.radians(x))))
print('O cosseno: {:.2f}'.format(math.cos(math.radians(x))) )
print('A tangente: {:.2f}'.format(math.tan(math.radians(x))))