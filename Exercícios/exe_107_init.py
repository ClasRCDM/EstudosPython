import exe_107 as moeda

print('{1}{0}{2}{3}'.format(f'{"_ Exercício/init 107 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
