print('{1}{0}{2}{3}'.format(f'{"_ Exercício 95 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

time, jogador, partidas = list(), dict(), list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    [partidas.append(int(input(f' - Quantos gols na partida {c}? '))) for c in range(0, tot)]

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy)

    while True:
        resp = str(input('Quer continuar? [S/N] ').upper())[0]
        if resp in 'SN': break
        print('ERRO! Responda Apenas S ou N.')

    if resp == 'N': break

print('{1}{2}{0}{2}{1}'.format(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.', '-=' * 15, '\n'))

[print(f' - => Na partida {i}, fez {v} gols.') for i, v in enumerate(jogador['gols'])]

print(f'Foi um total de {jogador["total"]} gols.')
