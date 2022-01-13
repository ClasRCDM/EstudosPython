print('{1}{0}{2}{3}'.format(f'{"_ Exercício 67 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

while True:
    val = int(
        input('[Para parar, digite um número negativo!]\nQuer ver a tabuada de qual valor? '))

    if val < 0: break

    for tab in range(1, 11): print(f'{tab} x {val:2} = {val*tab}')

print('FIM!!!')
