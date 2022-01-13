print('{1}{0}{2}'.format(f'{"_ Prints + Fors _":=^25}',
      '\033[4;33m<< ', ' >>\033[m'))

print('Printando uma lista:', ''.join([str(lst) for lst in range(11, 0, -1)]))

print('Printando uma lista:', end=' ')
for lst in range(1, 12):
    print(lst, end='')

print('\n', '-' * 10)

print(f'Printando uma lista: {[str(lst) for lst in range(11, 0, -1)]}')

print('Printando uma lista: {}'.format([str(lst) for lst in range(1, 12)]))
