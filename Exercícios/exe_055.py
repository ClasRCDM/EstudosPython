print('{1}{0} Desafio 55 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

maior = 0.0
menor = 0.0

for p in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))
