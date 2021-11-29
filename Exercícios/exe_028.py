from random import randint

print('{0} Desafio {0}'.format('=' * 10))

IA = randint(0, 5)

jogador = int(input('Descubra qual numero a IA jogou: [0 a 5] : '))

if jogador == IA:
    print('Você acertou PARÁBENS!')
else:
    print('I você errooouuu!!!')
