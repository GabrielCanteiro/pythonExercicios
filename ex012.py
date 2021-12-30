#ler o preço do produto e mostrar o valor com 5% de desconto
preco = int(input('Qual o preço deste produto?:'))
desconto = preco-(preco*0.05)
print('O preço do produto após o desconto de 5% é:R$ {}'.format(desconto))