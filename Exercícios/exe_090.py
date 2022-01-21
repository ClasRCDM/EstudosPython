print('{1}{0}{2}{3}'.format(f'{"_ Exercício 90 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

dicionario = {'nome': str(input('Nome: ')).strip()}

dicionario['média'] = float(input(f'Média de {dicionario["nome"]}: '))

print(f'Nome é igual a {dicionario["nome"]}\nMédia é igual a {dicionario["média"]}')
print('Situação é igual a', 'Aprovado.' if dicionario['média'] >= 6 else 'Reprovado.')
