print('{1}{0} Desafio 45 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

print('{}PARES{}'.format('\031[4;33m', '\033[m'))
for pares in range(0, 50):
    if pares // 2 == 0:
        print('{}{}{}'.format('\032[4;33m', pares, '\033[m'))
