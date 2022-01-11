print('{1}{0}{2}'.format(f'{" Exercício 67 ":=^25}', '\033[4;33m', '\033[m'))

while True:
    val = int(
        input('[Para parar, digitar um número negativo!]\nQuer ver a tabuada de qual valor? '))

    if val < 0: break

    for tab in range(1, 11):
        print(f'{tab} x {val:2} = {val*tab}')

print('FIM!!!')
