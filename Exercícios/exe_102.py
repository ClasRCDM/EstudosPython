print('{1}{0}{2}{3}'.format(f'{"_ Exercício 102 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))


def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1: print(' x ', end='')
            else: print(' = ', end='')
        f *= c
    return f


# -


