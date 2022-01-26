print('{1}{0}{2}{3}'.format(f'{"_ Exercício 98 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))


def contador(inicio, fim, passo=1):
    print('{2}{3}{0}{3}{1}'.format(
          f'Contagem de {inicio} até {fim} de {passo} em {passo}',
          ' - '.join([str(num) for num in range(inicio, fim, passo)]),
          '-=' * 20, '\n'))


# -

contador(1, 11)
contador(10, 0, -2)

print('{1}\n{0}'.format('Agora é a sua vez de personalizar a contagem!',
                        '-=' * 20))
ini = int(input('Início: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fi, pas)
