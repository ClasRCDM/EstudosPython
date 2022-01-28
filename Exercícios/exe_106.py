print('{1}{0}{2}{3}'.format(f'{"_ Exercício 106 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('{2}{1}{4}{0}{4}{1}{3}'.format(msg, '~' * tam, c[cor], c[0], '\n'))


# -
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM': break
    else: ajuda(comando)
titulo('ATÉ LOGO', 1)
