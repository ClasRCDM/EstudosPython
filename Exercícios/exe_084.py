print('{1}{0}{2}{3}'.format(f'{"_ Exercício 84 _":=^25}',
     '\033[4;33m<< ', ' >>\033[m', '\n'))

lista = list()
maior = menor = 0

while True:
    dado = list()
    dado.append(str(input('Nome: ')).strip())
    dado.append(int(input('Peso: ')))

    if len(lista) == 0: maior = menor = dado[1]
    else:
        if dado[1] > maior: maior = dado[1]
        elif dado[1] < menor: menor = dado[1]

    lista.append(dado[:])

    if str(input('Quer continuar? [S/N] ')).strip() in 'Ss': continue
    else: break

print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de', ' - '.join([str(nomes[0]) for nomes in lista if nomes[1] == maior]))
print(f'O menor peso foi de {menor}Kg. Peso de', ' - '.join([str(nomes[0]) for nomes in lista if nomes[1] == menor]))
