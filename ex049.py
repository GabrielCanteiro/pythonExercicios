'''
Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
'''
print('='*5+'TABUADA'+'='*5)
n = int(input('Escolha uma tabuada: '))
tabuada = 0
for c in range(1,11):
    tabuada += 1
    resultado = n * tabuada
    print('{} x {:2} = {}'.format(n, tabuada, resultado))
