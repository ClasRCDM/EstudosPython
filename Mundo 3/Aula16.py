print('{1}{0}{2}{3}'.format(f'{"_ Aula 16 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

# Não a necessidade de deixar entre Parênteses|() para ser uma tupla
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'  # Tuplas são imutáveis

print('Os lanches são:', ' - '.join([str(lanches) for lanches in lanche]))
print('Os lanches são:', ' - '.join([str(lanches) for lanches in lanche][:2]))
print('Os lanches são:', ' - '.join([str(lanches) for lanches in lanche][::-1]))
