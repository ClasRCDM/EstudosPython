print('{1}{0} Desafio 36 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

casa = float(input('Valor da casa: R$\033[32m'))
salario = float(input('\033[mSalário do comprador: R$\033[32m'))
anos = int(input('\033[mQuantos anos de financiamento? \033[32m'))

prestacao = casa / (anos * 12)

print('\033[33mPara pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R${:.2f}'.format(prestacao))

minimo = salario * 30 / 100

if prestacao <= minimo:
    print('Empréstimo pode ser {}CONCEDITO{}!'.format('\033[4m', '\033[m'))
else:
    print('Empréstimo NEGADO!!'.format('\033[4m', '\033[m'))
