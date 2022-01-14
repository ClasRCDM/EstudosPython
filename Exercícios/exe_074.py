from random import sample

print('{1}{0}{2}'.format(f'{"_ Exercício 74 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m'))

tupla = tuple((sample(range(0, 11), 5)))

print('Foram gerados os números:',
      ' - '.join([str(numeros) for numeros in tupla]))
print(f'O maior número é {max(tupla)} e o menor {min(tupla)}')
