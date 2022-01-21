from datetime import datetime

print('{1}{0}{2}{3}'.format(f'{"_ Exercício 92 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

dicionario = {'nome': str(input('Nome: ')).strip(),
              'idade': datetime.now().year - int(input('Ano de Nascimento: ')),
              'ctps': int(input('Carteira de Trabalho (0 não tem): '))}

if dicionario['ctps'] != 0:
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['salário'] = float(input('Salário: R$'))
    dicionario['aposentadoria'] = dicionario['idade'] + ((dicionario['contratação'] + 35) - datetime.now().year)

[print(f' - {k} tem o valor {v}') for k, v in dicionario.items()]
