print('{1}{0}{2}{3}'.format(f'{"_ Exercício 80 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

lista = list()

while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        print('Valor adicionado com sucesso...')
        lista.append(valor)
    else: print('Valor duplicado! Não adicionado...')

    if str(input('Quer continuar? [S/N] ')).strip()[0] in 'Ss': continue
    else: break

print('-=' * 15)
print('Você digitou os valores:', ' - '.join([str(valores) for valores in sorted(lista)]))
