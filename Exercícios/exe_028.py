from random import randint
from time import sleep

print('{0} Desafio 28 {0}'.format('=' * 10))

IA = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Descubra qual numero a IA jogou: [0 a 5] : '))

print('PROCESSANDO...')
sleep(2)

if jogador == IA:
    print('Você acertou PARABÉNS!')
else:
    print('I você errooouuu!!!')
    print('GANHEI!! Eu pensei no número {}'.format(IA))
