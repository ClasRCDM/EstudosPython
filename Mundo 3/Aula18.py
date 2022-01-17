print('{1}{0}{2}{3}'.format(f'{"_ Aula 18 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

lista = list()

lista.append('Raphael')
lista.append(40)

galera = list()

galera.append(lista[:])

lista[0] = 'Jão'
lista[1] = 22

galera.append(lista[:])

galerinha = [['Ala', 1], ['Apo', 2], ['Carai', 3]]

print(galera)
print(galerinha[2][1])

for p in galerinha:
    print(f'{p[0]}, index {p[1]}.')
