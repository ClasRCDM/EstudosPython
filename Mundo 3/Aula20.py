print('{1}{0}{2}{3}'.format(f'{"_ Aula 20 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))


def lin():
    print('-' * 30)


def linsimples(msg):
    lin()
    print(f' - {msg}')
    lin()


def lincomplex(msg):
    print('{1}{2}{0}{1}'.format(f' - {msg}', '-' * 30, '\n'))


def somasimples(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


def somacomplex(a, b):
    return print('{0}{2}{1}'.format(f'A = {a} e B = {b}',
                                    f'A soma A + B = {a + b}', '\n'))


# Empacotamento de valores
def contadorsimples(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


def contadorcomplex(*num):
    print('Recebi os valores',
          ', '.join(str(nu) for nu in num),
          f'e são ao todo {len(num)} números.')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] += 2
        pos += 1


# Programa Principal

linsimples('CURSO EM VÍDEO')
lincomplex('CURSO EM VÍDEO\n')

somasimples(4, 5)
lin()
somacomplex(8, 9)

lin()

contadorsimples(2, 1, 7)
lin()
contadorcomplex(4, 4, 7, 6, 2)

lin()

valores1 = [2, 4, 8, 10, 12]
valores2 = [2, 4, 8, 10, 12]

dobra(valores1)
print(valores1)
