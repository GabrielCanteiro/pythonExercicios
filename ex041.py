'''
Ex Python 041: A confederação nacional de natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.
-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JÚNIOR
-Até 20 anos: SÊNIOR
-Acima: MASTER
'''
import datetime
print('~~~|~~~~'*7)
print('Categorizando os atletas de acordo com suas idades')
print('~~~|~~~~'*7)

ano = int(input('Qual ano de nascimento do atleta?'))
anoatual = datetime.date.today().year

if anoatual - ano <= 9:
    print('Este é um atleta MIRIM')

elif anoatual - ano > 9 and anoatual - ano <= 14:
    print('Este é um atleta INFANTIL')

elif anoatual - ano > 14 and anoatual - ano <= 19:
    print('Este é um atleta JÚNIOR')

elif anoatual - ano > 19 and anoatual - ano <= 25:
    print('Este é um atleta SÊNIOR')

elif anoatual - ano > 25:
    print('Este é um atleta MASTER')

print('Este atleta possui {} anos'.format(anoatual - ano))