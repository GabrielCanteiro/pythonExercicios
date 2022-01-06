'''
Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos.
'''
contidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    contidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

print('A média de idade do grupo é de {} anos'.format(contidade/p))
print('O homem mais velho é {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('O total de {} mulheres sao menores de 20 anos'.format(totmulher20))