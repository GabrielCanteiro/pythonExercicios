'''
Ex Pyhton 039: Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar
-Se é a hora de se alistar
-Se já passou do tempo do alistamento
Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo
'''
import datetime
print('▃_︻┻═┳一¨¨¨¨¨¨'*1)
print('Descubra agora qual seu status no Alistamento militar ¬¬')

ano = int(input('Qual ano do seu nascimento '))
atual = datetime.date.today().year
idade = atual - ano

if idade == 18:
    print('Você deverá se alistar neste ano!')
elif idade > 18:
    saldo = idade - 18
    print('O seu alistamento foi há {} anos'.format(saldo))
elif idade < 18:
    saldo = 18 - idade
    print('Você deverá se alistar daqui {} anos em {}'.format(saldo,atual+saldo))

