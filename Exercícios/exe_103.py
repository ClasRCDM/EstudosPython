print('{1}{0}{2}{3}'.format(f'{"_ Exercício 103 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))


def ficha(jog='<não informado>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# -

n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))

if g.isnumeric(): g = int(g)
else: g = 0
if n.strip() == '': ficha(gol=g)
else: ficha(n, g)
