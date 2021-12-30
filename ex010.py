#Calcular quantos dolares uma pessoa pode comprar com o que tem na carteira $=3,27
x = int(input('Saldo da carteira: '))
dolar = x/3.27
print('Com R${} é possivel comprar ${:.2f}'.format(x,dolar))