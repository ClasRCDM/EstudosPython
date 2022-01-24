print('{1}{0}{2}{3}'.format(f'{"_ Exercício 94 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

pessoa, galera = dict(), list()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ').upper())[0]
        if resp in 'SN':
            break
        print('ERRO! Responda Apenas S ou N.')

    if resp == 'N': break

print('{0}{2}{1}{0}'.format('-=' * 30, f'A) Ao todo temos {len(galera)} pessoas cadastradas.', '\n'))

media = soma / len(galera)
print(f'B) A média de idade é de {media:2.0f}')

print('C) As mulheres cadastradas foram ', end='')
'''for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')'''
[print(f'{p["nome"]} ', end='') for p in galera if p['sexo'] in 'Ff']

print('D) Lista das pessoas que estão acima da média: ')
'''for p in galera:
    if p['idade'] >= media:
        print(' - ', end='')
        [print(f'{k} = {v}; ', end='') for k, v in p.items()]'''
print(' - ', end='')
[[print(f'{k} = {v}; ') for k, v in p.items()] for p in galera if p['idade'] >= media]

print('<< ENCERRADO >>')
