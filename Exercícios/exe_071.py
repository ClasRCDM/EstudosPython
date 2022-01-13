print('{1}{0}{2}{3}'.format(f'{"_ Exercício 71 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

total = valor = int(input('Que valor você quer sacar? R$'))

ced, totced = 50, 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0: print(f'Total de {totced} cédulas de R${ced} reais')
        if ced == 50: ced = 20
        elif ced == 20: ced = 10
        elif ced == 10: ced = 1
        totced = 0
        if total == 0: break

print('Volte sempre ao BANCO CEV! Tenha um BOM DIA!')
