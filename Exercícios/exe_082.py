print('{1}{0}{2}{3}'.format(f'{"_ Exercício 82 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))

    if str(input('Quer continuar? [S/N] ')).strip()[0] in 'Ss': continue
    else: break

print('-=' * 15)
print('A lista completa é', ' - '.join([str(numeros) for numeros in lista]))
print('A lista de pares é', ' - '.join([str(numeros) for numeros in lista if numeros % 2 == 0]))
print('A lista de ímpares é', ' - '.join([str(numeros) for numeros in lista if numeros % 2 != 0]))
