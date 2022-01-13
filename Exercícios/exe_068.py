from random import randint

print('{1}{0}{2}{3}'.format(f'{"_ Exercício 68 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

v = 0

while True:

    player = int(input('Diga um valor: '))
    IA = randint(0, 11)
    total = player + IA

    tipo = ' '
    while tipo not in 'PI': tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador {IA}. Total de {total}', end=' ')
    print('Deu PAR!' if total % 2 == 0 else 'Deu ÍMPAR!')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!')
        else:
            print('Você PERDER!!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
        else:
            print('VOcê PERDEU!!!!')
            break
    v += 1

    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes.')
