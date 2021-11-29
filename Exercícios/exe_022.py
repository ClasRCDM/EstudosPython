print('{0} Desafio 22 {0}'.format('=' * 10))

nome = str(input('Escreva seu nome: ')).strip()

print('O seu nome maiúsculo fica {}'.format(nome.upper()))
print('O seu nome minúsculo fica {}'.format(nome.lower()))

nome_nospace = nome.split()
junto = ''.join(nome_nospace)

print('Ao todo seu nome contem {} letras'.format(len(junto)))
print('O primeiro nome tem {} letras'.format(len(nome_nospace[0])))
