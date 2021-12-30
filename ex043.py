'''
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''
print('--'*10)
print('Calculo de IMC')
print('--'*10)

altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em Kg: '))
imc = peso / (altura**2)
cor = '\033[1;33m'
if imc < 18.5:
    print('O paciente está {}abaixo do peso'.format(cor))
elif imc >= 18.5 and imc < 25:
    print('O paciente está no {}Peso Ideal'.format(cor))
elif imc > 25 and imc < 30:
    print('O paciente está em {}Sobrepeso'.format(cor))
elif imc > 30 and imc < 40:
    print('O paciente está em estado de {}Obesidade'.format(cor))
elif imc > 40:
    print('O paciente está em estado de {}Obesidade Mórbida'.format(cor))

print('imc = {:.2f}'.format(imc))