print('{1}{0} Desafio 49 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

for tabuada in range(11):
    print('{3}{0} {5}x{6} {1:2}{7}:{8} {9}{2}{4}'.format(
        2, tabuada, tabuada * 2,
        '\033[36m', '\033[m',
        '\033[35m', '\033[36m',
        '\033[32m', '\033[36m',
        '\033[37m'))
else:
    print('{}FIM{}'.format('\033[4;31m', '\033[m'))
