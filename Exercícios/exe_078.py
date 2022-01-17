print('{1}{0}{2}{3}'.format(f'{"_ Exercício 78 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

lista = list()

for numeros in range(5): lista.append(int(input(f'Digite o {numeros+1}°: ')))
else:
    print(f'O maior número foi {max(lista)}.')
    print(f'O menor número foi {min(lista)}.')
    [print(f'O número {numero} está no index: {index}') for index, numero in enumerate(lista)]
