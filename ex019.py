#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
alunos = ['João','Gabriel','Beatriz','Bianca']
print('{} irá apagar o quadro'.format(random.choice(alunos)))