print('{1}{0}{2}'.format(f'{"_ Exercício/Módulo 108 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m'))


def metade(prc):
    return prc / 2


def dobro(db):
    return db * 2


def aumentar(v, am):
    return am / 100 * v + v


def diminuir(v, dm):
    return (dm / 100 * v - v) * -1


def moeda(v):
    return f'R${v:.2f}'.replace('.', ',')
