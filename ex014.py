#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Qual a temperatura atual?: '))
f = (c * 9/5) + 32
print('{}ºC é equivalente a {:.1f}ºF'.format(c,f))