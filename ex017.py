#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
cO = float(input('Digite o cateto oposto: '))
cA = float(input('digite o cateto adjacente: '))
#opção 1
#somaCatetos = (cA**2) + (cO**2)
#hip = math.sqrt(somaCatetos)
#print('{}² + {}² = hip²\n portanto:\nhip = {:.2f}'.format(cO,cA,hip))

#opção2
hip = math.hypot(cO,cA)
print('A hipotenusa vai medir {:.2f}'.format(hip))