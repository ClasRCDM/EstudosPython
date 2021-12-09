print('{1}{0} Desafio 52 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

n = int(input('Dígite um número: '))
tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
        print('{}'.format('\033[33m'), end='')
    else:
        print('{}'.format('\033[31m'), end='')
    print('{}'.format(c), end=' ')

print('\n\033[37mO número {} foi divisível {} vezes'.format(n, tot))

if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso não é PRIMO')
