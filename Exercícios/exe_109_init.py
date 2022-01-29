import exe_109 as moeda

print('{1}{0}{2}{3}'.format(f'{"_ Exercício/init 109 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, False)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
