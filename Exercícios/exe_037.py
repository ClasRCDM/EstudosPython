print('{1}{0} Desafio 37 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

numero = int(input('Um numero para converter: \033[32m'))

print('\033[31mEscolha entre Binário, Octal e Hexadecimal\033[m')
conversao = str(input('Qual: \033[32m')).strip().title()

if conversao in 'Binário Binario':
    print('{}, Se torna {}'.format(numero, binario))
elif conversao == 'Octal':
    pass
elif conversao == 'Hexadecimal':
    pass
