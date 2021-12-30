'''
Ex Python 040: Crie um programa que leia duas notas de um aluno e caulcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO
'''
print('-_'*10)
print('Calculo de média')
print('-_'*10)

n1 = float(input('Nota da primeira prova: '))
n2 = float(input('Nota da segunda prova: '))
m = (n1 + n2) / 2

if m < 5:
    print('Média = {} - REPROVADO!'.format(m))
elif m > 5 and m < 7:
    print('Média = {} - RECUPERAÇÃO!'.format(m))
elif m >= 7:
    print('Média = {} - APROVADO!'.format(m))
