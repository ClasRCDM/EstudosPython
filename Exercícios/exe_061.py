print('{1}{0} Desafio 61 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

prim = int(input('Primeiro termo: '))
razão = int(input('Razão de PA: '))

termo = prim
cont = 1

while cont <= 10:
    print(f'{termo} > ', end='')

    termo += razão
    cont += 1
else:
    print('FIM')
