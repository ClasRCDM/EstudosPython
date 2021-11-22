print('=' * 5, 'Aula 06', '=' * 5)
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
# print('A soma entre', n1, 'e', n2, 'vale', n1+n2)
print('\nA soma entre {} e {} vale {}'.format(n1, n2, n1+n2))
# ou
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, n1+n2))
# ou
print('A soma é {2}, entre {1} e {0}\n'.format(n1, n2, n1+n2))

n = float(input('Digite um valor: '))
print(n)

b = bool(input('Digite algo: '))  # Se tiver valor é True, vazia é False
print(b)
