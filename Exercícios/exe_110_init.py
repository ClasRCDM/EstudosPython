import exe_110 as moeda

print('{1}{0}{2}{3}'.format(f'{"_ Exercício/init 110 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 80, 35)
