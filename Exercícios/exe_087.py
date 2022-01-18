print('{1}{0}{2}{3}'.format(f'{"_ Exercício 87 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

lista = list(([0, 0, 0], [0, 0, 0], [0, 0, 0]))

for x in range(len(lista)):
    for y in range(len(lista)):
        lista[x][y] = int(input(f'Digite um valor para [{x}, {y}]: '))
else:
    soma_pares = soma_3coluna = maior_segunda = 0

    for x in range(len(lista)):
        for y in range(len(lista)):
            print(f'[  {lista[x][y]:^5} ]', end='')
            if lista[x][y] % 2 == 0:
                soma_pares += lista[x][y]
        print()
    else:
        print(f'A soma de todos os valores pares é {soma_pares}.')

    for x in range(len(lista)): soma_3coluna += lista[x][2]
    else: print(f'A soma dos valores da terceira coluna é {soma_3coluna}.')

    for y in range(len(lista)):
        if y == 0: maior_segunda = lista[1][y]
        elif lista[1][x] > maior_segunda: maior_segunda = lista[1][x]
    else: print(f'O maior valor da segunda linha é {maior_segunda}')
