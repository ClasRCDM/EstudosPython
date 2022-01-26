print('{1}{0}{2}{3}'.format(f'{"_ Exercício 96 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


# -

print('{}{}{}'.format('Controle de terrenos', '\n', '-' * 20))
la = float(input('LARGURA (m): '))
co = float(input('COMPRIMENTO (m): '))
area(la, co)
