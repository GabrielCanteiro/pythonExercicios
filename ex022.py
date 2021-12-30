#Cire um programa que leie o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiusculas. Com todas as letras minúsculas.
# Quantas letras tem ao todo,sem considerar espaços.
# Quantas letras tem o primeiro nome
nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
qnt = len(nome.replace(' ',''))
print('Há um total de {} letras'.format(qnt))
dividir = nome.split()
qntletras = len(dividir[0])
print('O primeiro nome possui {} letras'.format(qntletras))
