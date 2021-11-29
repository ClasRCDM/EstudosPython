print('{0} Desafio {0}'.format('=' * 10))

salario = float(input('Salário: R$'))

calculo = 0

if salario > 1250:
    print('Aumento de 10%')
    calculo = salario * 10/100 + salario
else:
    print('Aumento de 15%')
    calculo = salario * 10/100 + salario

print('Você recebera um aumento de R${}'.format(calculo))
