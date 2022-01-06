from random import randint

print('{1}{0} Desafio 58 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

IA = randint(0, 10)

tentativas = 0

num = int(input('Tente adivinhar [0/10]: '))
while num != IA:
    print('\nVocê errou, tente novamente - [0/10]!!!')
    tentativas += 1

    if num < IA:
        print('Maior... Tente de novo.\n')
    elif num > IA:
        print('Menor... Tente outro.\n')

    num = int(input('Tente adivinhar [0/10] '))

else:
    tentativas += 1
    print('Você acertou!!',
          f'Com {tentativas} tentativas.'
          if tentativas > 1 else
          f'Com {tentativas} tentativa.')
