print('{0} Aula 12 {0}'.format('=' * 10))

nome = str(input('Qual é seu nome? '))

if nome == 'Raphael':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Que nome popular')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome FEMININO!!')
else:
    print('Seu nome é normal')

print('Tenha um bom dia, \033[31m{}\033[m'.format(nome))
