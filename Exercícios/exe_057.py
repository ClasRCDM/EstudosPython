print('{1}{0} Desafio 57 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

sexo = str(input('Qual o seu sexo? {}[M/F]{} '.format('\033[4;33m', '\033[32m'))).strip().upper()
while sexo not in 'MF':
    print('{}Porfavor apenas [F/M]!!{}'.format('\033[4;34m', '\033[m'))
    sexo = str(input('Qual o seu sexo? {}[M/F]{} '.format('\033[4;33m', '\033[32m'))).strip().upper()
else:
    print('Obrigado por responder!')
