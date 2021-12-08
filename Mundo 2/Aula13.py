print('{1}{0} Aula 13 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

for c in range(1, 7):
    print('ALA {}'.format(c))
else:
    print('Minha rolas')
    print('')

for c in range(1, 7, 2):
    print('ALA {}'.format(c))
else:
    print('Minha rolas')
    print('')

for c in range(6, 0, -1):
    print('ALA {}'.format(c))
else:
    print('Minha rolas')
    print('')

n = int(input('Dígite um número: '))
for c in range(1, n+1):
    print('ALA {}'.format(c))
else:
    print('Minha rolas')
    print('')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print('ALA {}'.format(c))
else:
    print('Minha rolas')
    print('')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
else:
    print('O somatório de todos os valores foi {}'.format(s))
