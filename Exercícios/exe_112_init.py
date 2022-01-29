import exe_112 as moeda

print('{1}{0}{2}{3}'.format(f'{"_ Exercício/init 112 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

p = moeda.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 35)
