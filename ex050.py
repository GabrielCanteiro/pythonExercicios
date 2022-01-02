'''
Exercício Python 050: Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0
contvalido = 0
continvalido = 0
for c in range(1,7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        contvalido += 1
    continvalido +=1
print('Você informou {} numeros, porém apenas {} são válidos, portanto a soma foi {}'.format(continvalido,contvalido,soma))

