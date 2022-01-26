print('{1}{0}{2}{3}'.format(f'{"_ Exercício 97 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))


def escreva(msg):
    tam = len(msg) + 2
    print('{1}{2}{0}{2}{1}'.format(f' {msg} ', '~' * tam, '\n'))


escreva('Gustavo Guanabara')
escreva('Raphael')
escreva('Deus__')
