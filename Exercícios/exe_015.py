print('{0} Desafio 15 {0}'.format('=' * 10))
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? Km'))
pago = dias * 60 + km * 0.15
print('O total a pagar é de R${:.2f}'.format(pago))
