print('{1}{0}{2}{3}'.format(f'{"_ Exercício 86 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

lista = list(([0, 0, 0], [0, 0, 0], [0, 0, 0]))

for x in range(len(lista)):
    for y in range(len(lista)):
        lista[x][y] = int(input(f'Digite um valor para [{x}, {y}]: '))
else:
    for x in range(len(lista)):
        for y in range(len(lista)):
            print(f'[  {lista[x][y]:^5} ]', end='')
        print()
