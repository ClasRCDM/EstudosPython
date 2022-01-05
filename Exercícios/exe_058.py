from random import randint

print('{1}{0} Desafio 58 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

IA = randint(0, 10)

tentativas = 0

num = int(input('Tente adivinhar [0/10] '))
while num != IA:
    print('Você errou, tente novamente - [0/10]!!!')
    tentativas += 1
    num = int(input('Tente adivinhar [0/10] '))
else:
    print(f'Você acertou!!, Com {tentativas} tentativas.')
