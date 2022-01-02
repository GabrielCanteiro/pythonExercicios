'''
Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''
frase = input('Digite uma frase: ').strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print(inverso)
if junto == inverso:
    print('Que legal "{}" é um palindromo '.format(inverso))
else:
    print('Não é um palíndromo ')