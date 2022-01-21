print('{1}{0}{2}{3}'.format(f'{"_ Exercício 93 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

jogador = {'nome': str(input('Nome do Jogador: ')).strip()}
partidas = list()

tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
'''for c in range(0, tot):
    partidas.append(int(input(f' - Quantos gols na partida {c+1}? ')))'''
[partidas.append(int(input(f' - Quantos gols na partida {c+1}? '))) for c in range(0, tot)]

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('{1}{0}{1}'.format(jogador, '-=' * 15))

'''for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')'''
[print(f'O campo {k} tem o valor {v}') for k, v in jogador.items()]

print('{1}{0}{1}'.format(
    f' O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas ', '-=' * 5))

'''for i, v in enumerate(jogador['gols']):
    print(f' - => Na partida {i}, fez {v} gols.')'''
[print(f' - => Na partida {i}, fez {v} gols.') for i, v in enumerate(jogador['gols'])]    

print(f'Foi um total de {jogador["total"]} gols.')
