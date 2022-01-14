print('{1}{0}{2}'.format(f'{"_ Exercício 77 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m'))

tupla = 'seila', 'porra', 'mano', 'ala', 'caralho', 'cansei'

for p in tupla:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
