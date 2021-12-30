'''
Faça um programa que leia uma frase pelo teclado e mostre:
>Quantas vezes aparece a letra "A"
>Em que posição ela aparece a primeira vez
>Em que posição ela aparece a ultima vez
'''
frase = input('Digite uma frase: ').lower().strip()
print('A letra "A" aparece {}x'.format(frase.count('a')))
print('A primeira letra "A" está na posição: {}'.format(frase.find('a')+1))
print('A ultima letra "A" está na posição: {}'.format(frase.rfind('a')+1))