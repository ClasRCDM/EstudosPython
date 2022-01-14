print('{1}{0}{2}'.format(f'{"_ Exercício 76 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m'))

tupla = tuple(('Pão', 1,
              'leite', 3.5,
              'Caderno', 15.9))

for pos in range(0, len(tupla)):
    if pos % 2 == 0: print(f'{tupla[pos]:.<30}', end='')
    else: print(f'R${tupla[pos]:>7.2f}')
