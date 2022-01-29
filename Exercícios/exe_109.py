print('{1}{0}{2}'.format(f'{"_ Exercício/Módulo 109 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m'))


def metade(prc, formata=False):
    cont = prc / 2
    return cont if not formata else moeda(cont)


def dobro(db, formata=False):
    cont = db * 2
    return cont if not formata else moeda(cont)


def aumentar(v, am, formata=False):
    cont = am / 100 * v + v
    return cont if not formata else moeda(cont)


def diminuir(v, dm, formata=False):
    cont = (dm / 100 * v - v) * -1
    return cont if not formata else moeda(cont)


def moeda(v):
    return f'R${v:.2f}'.replace('.', ',')
