print('{1}{0} Desafio 37 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

numero = int(input('Um numero para converter: \033[32m'))

print('\033[31mEscolha entre Binário, Octal e Hexadecimal\033[m')
conversao = str(input('Qual: \033[32m')).strip().title()

if conversao in 'Binário Binario':
    print('{}, Se torna {} em Binário'.format(numero, bin(numero)))
elif conversao == 'Octal':
    print('{}, Se torna {} em Octal'.format(numero, oct(numero)))
elif conversao == 'Hexadecimal':
    print('{}, Se torna {} em hexadecimal'.format(numero, hex(numero)))
else:
    print('Opção inválida. Tente novamente')
