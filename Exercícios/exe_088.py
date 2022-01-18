from random import randint
from time import sleep

print('{1}{0}{2}{3}'.format(f'{"_ Exercício 88 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

lista, jogos = list(), list()

quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6: break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('{1}{0}{1}'.format(f' SORTEANDO {quant} JOGOS ', '-=' * 3))

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
else: print('{1}{0}{1}'.format(f' < BOA SORTE! > ', '-=' * 5))
