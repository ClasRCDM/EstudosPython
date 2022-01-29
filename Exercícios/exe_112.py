print('{1}{0}{2}'.format(f'{"_ Exercício/Módulo 112 _":=^25}',
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


def resumo(v, au, red, fo=True):
    print('{1}{2}{0:^35}{2}{1}'.format('RESUMO DO VALOR', '-' * 35, '\n'))
    print(f'Preço Analisado: {moeda(v):>4}')
    print(f'Metade do preço: {metade(v, fo):>4}')
    print(f'Dobro do preço: {dobro(v, fo):>4}')
    print(f'{au}% de aumento: {aumentar(v, au, fo):>4}')
    print(f'{red}% de redução: {diminuir(v, red, fo):>4}')
    print('-' * 35)


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '': print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido.\033[m')
        else:
            valido = True
            return float(entrada)
