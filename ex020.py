#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
alunos = ['João','Gabriel','Beatriz','Bianca']
random.shuffle(alunos)
print('irão se apresentar {}, respectivamente.'.format(alunos))