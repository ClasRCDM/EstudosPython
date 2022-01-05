print('{1}{0} Desafio 59 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

nu1 = int(input('Primeiro valor: '))
nu2 = int(input('Segundo valor: '))

print('''
[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos números
[ 5 ] - Sair do programa
''')

valor = int(input('Selecione uma opção: '))
while valor != 5:
    if valor == 1:
        print(f'A soma entre {nu1} e {nu2} é {nu1+nu2} <')
        break
    elif valor == 2:
        print(f'A multiplicação entre {nu1} e {nu2} é {nu1*nu2} <')
        break
    elif valor == 3:
        maior = nu1 if nu1 > nu2 else nu2
        print(f'Entre {nu1} e {nu2} o maior número é {maior}')
        break
    elif valor == 4:
        print('\nNovamente...')
        nu1 = int(input('Primeiro valor: '))
        nu2 = int(input('Segundo valor: '))

    valor = int(input('Selecione uma opção: '))

print('fim do programa!')
