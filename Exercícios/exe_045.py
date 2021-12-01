from random import randint

print('{1}{0} Desafio 45 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

itens = ('Pedra', 'Papel', 'Tesoura')
IA = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

if not jogador >= 3:
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[IA]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)
else:
    print('Numero invalido, tente novamente!')

if IA == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif IA == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif IA == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
