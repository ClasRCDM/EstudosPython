print('{0} Desafio 27 {0}'.format('=' * 10))

nome = str(input('Seu nome: '))

lista = nome.split()
primeiro = lista[0]
ultimo = lista[-1]

print('''O primeiro nome é {}
O ultimo é {}'''.format(primeiro, ultimo))
