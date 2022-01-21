from operator import itemgetter
from random import randint
from time import sleep

print('{1}{0}{2}{3}'.format(f'{"_ Exercício 91 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

dicionario = {'jogador1': randint(1, 6),
              'jogador2': randint(1, 6),
              'jogador3': randint(1, 6),
              'jogador4': randint(1, 6)}

print('Valores sorteados:')

[print(f'{k} tirou {v} no dado.') for k, v in dicionario.items()]
sleep(1)

ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print('{0}{1}{0}'.format('-=' * 15, ' == RANKING DOS JOGADORES == '))

[print('.'*32, f'{i+1}° lugar: {v[0]} com {v[1]}.') for i, v in enumerate(ranking)]
sleep(1)
