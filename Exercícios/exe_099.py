print('{1}{0}{2}{3}'.format(f'{"_ Exercício 99 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))


def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0: maior = valor
        else:
            if valor > maior: maior = valor
        cont += 1
    print('{}\n{}\n'.format(f'Foram informados {cont} valores ao todo.',
                          f'O mairo valor informado foi {maior}.'))


# -

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
