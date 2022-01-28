print('{1}{0}{2}{3}'.format(f'{"_ Exercício 102 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n : O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1: print(' x ', end='')
            else: print(' = ', end='')
        f *= c
    return f


# -

print(fatorial(5, show=True))
print(fatorial(5))
