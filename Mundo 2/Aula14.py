print('{1}{0} Aula 14 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

c = 1
while c < 10:
    print(c)
    c += 1
else:
    print('fim')

r = 's'
while r == 's':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).lower().strip()
else:
    print('Fim')
