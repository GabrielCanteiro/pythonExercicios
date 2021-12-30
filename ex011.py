#calcular a area de uma parede e o quanto de tinta é necessario para pinta-la cada litro de tinta pinta 2m2
h = float(input('Qual a Altura da parede?'))
l = float(input('Qual a Largura da parede?'))
a = l*h
qnt = a/2
print('Sua parede possui uma área de {}m²\nSerá necessário {}L de tinta para ser pintada'.format(a,qnt))