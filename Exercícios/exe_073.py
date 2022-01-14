print('{1}{0}{2}'.format(f'{"_ Exercício 73 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m'))

tupla = ('Botafogo', 'Goiás', 'Coritiba', 'Avaí', 'CSA',
         'Guarani', 'CRB', 'Náutico', 'Vila Nova', 'Vasco da Gama',
         'Ponte Preta', 'Operário', 'Brusco', 'Cruzeiro', 'Sampaio Corrêa',
         'Londrina', 'Remo-PA', 'Vitória', 'Confiança', 'Brasil')

print('{1}{0}{2}{3}'.format(f'{"_ Brasileirão 2021 _":=^25}',
      '\033[4;32m>> ', ' <<\033[m', '\n'))

print('Os 5 primeiros colocados:',
      ' - '.join([str(primeiros5) for primeiros5 in tupla[:5]]))
print('Os últimos 4 colocados são:',
      ' - '.join([str(primeiros5) for primeiros5 in tupla[:-5:-1]]))
print('\nEm ordem alfabética:',
      f'\n{"-" * 21}'.join([str(primeiros5) for primeiros5 in sorted(tupla)]))
print(f'\nA Chapecoense esta na posição {tupla.index("Chapecoense")+1} do Brasileirão'
      if 'Chapecoense' in tupla else
      '\nA Chapecoense não esta no Brasileirão de 2021')
