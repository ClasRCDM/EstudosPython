print('{1}{0}{2}{3}'.format(f'{"_ Exercício 85 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

lista = list(([], []))
print(lista)

for valor in range(7):
    dado = int(input(f'Digite o {valor}° valor: '))

    if dado % 2 == 0: lista[0].append(dado)
    elif dado % 2 != 0: lista[1].append(dado)
else: print(f'{sorted(lista[0])}\n{sorted(lista[1])}')
