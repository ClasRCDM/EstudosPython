print('{1}{0}{2}{3}'.format(f'{"_ Aula 18 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

dicionario = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

print(dicionario)
print(dicionario.values())
print(dicionario.keys())
print(dicionario.items())

print(f'O {dicionario["nome"]} tem {dicionario["idade"]} anos')

for k, v in dicionario.items():
    print(f'{k} = {v}')
