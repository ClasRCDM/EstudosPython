import uteis

print('{1}{0}{2}{3}'.format(f'{"_ Aula 22 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

# -

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
