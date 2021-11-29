print('{0} Desafio {0}'.format('=' * 10))

frase = str(input('Uma frase: '))

vezes = frase.count('a')
posicao = frase.find('a')
posição_final = frase.rfind('a')

print('''A letra a aparace {} vezes,
na posição inicial {},
e na posição final {}'''.format(vezes, posicao, posição_final))
