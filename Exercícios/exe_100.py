from random import randint

print('{1}{0}{2}{3}'.format(f'{"_ Exercício 100 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))


def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
    else: print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0: soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.')


# -

numeros = list()
sorteia(numeros)
somaPar(numeros)
