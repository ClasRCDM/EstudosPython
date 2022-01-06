from math import factorial

print('{1}{0} Desafio 60 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

n = int(input('Digite um número para calcular ser factorial: '))
f = factorial(n)

print('O fatorial de {n} é {f}.')
