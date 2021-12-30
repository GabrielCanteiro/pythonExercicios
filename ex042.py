'''
Ex Python 042: Refaça o exercicio 025 dos triangulos.
acrescentando o recurso de mostrar que tipo de triangulo será formado:
-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes
'''
print('-=-'*20)
print('Analisador e classificador de Triângulos')
print('-=-'*20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and b + c > a and c + a > b:
    print('Dessa forma é possivel formar um triangulo')
    if a == b == c:
        print('Equilátero')
    if a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Asssim não é possivel formar um triangulo')


'''if a == b and a == c:
    print('Este é um triangulo Equilátero')
elif a != b and b != c and c != a:
    print('Este é um triangulo Escaleno')
elif a == b or a == c or b == c and a != b or a != c or b != c:
    print('Este é um triangulo Isosceles')'''