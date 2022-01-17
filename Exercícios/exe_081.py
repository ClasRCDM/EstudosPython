print('{1}{0}{2}{3}'.format(f'{"_ Exercício 81 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))

    if str(input('Quer continuar? [S/N] ')).strip()[0] in 'Ss': continue
    else: break

print(f'Você digitou {len(lista)} elementos!')
print('Os valores em ordem decrescente são', ' - '.join([str(numeros) for numeros in sorted(lista, reverse=True)]))
