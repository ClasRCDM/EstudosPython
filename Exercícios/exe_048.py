print('{1}{0} Desafio 48 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

print('{}IMPARES múltiplos de três{}'.format('\033[4;31m', '\033[m'))

soma = 0
contador = 0

for impares in range(1, 501, 2):
    if impares % 3 == 0:
        soma += impares
        contador += 1

        print('{}{}{}'.format('\033[4;35m', impares, '\033[m'), end=' ')

print('\nA soma de todos os {} valores solicitados é {}'.format(contador, soma))
