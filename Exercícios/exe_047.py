print('{1}{0} Desafio 47 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

print('{}PARES{}'.format('\033[4;31m', '\033[m'))
for pares in range(2, 51, 2):
    if pares % 2 == 0:
        print('{}{}{}'.format('\033[4;35m', pares, '\033[m'), end=' ')
