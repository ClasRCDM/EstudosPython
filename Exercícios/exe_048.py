print('{1}{0} Desafio 45 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

print('{}IMPARES múltiplos de três{}'.format('\033[4;31m', '\033[m'))
for pares in range(1, 501):
    if pares % 2 != 0 and pares % 3 == 0:
        print('{}{}{}'.format('\033[4;35m', pares, '\033[m'), end=' ')
