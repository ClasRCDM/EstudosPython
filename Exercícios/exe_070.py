print('{1}{0}{2}{3}'.format(f'{"_ Exercício 70 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

total = totmil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))

    cont += 1
    total += preco

    if preco > 1000: totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN': resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resp == 'N': break

print(f'{"Fim do PROGRAMA":-^40}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
