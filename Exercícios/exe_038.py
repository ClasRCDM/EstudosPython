print('{1}{0} Desafio 38 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

numero1 = int(input('Numero 1: \033[32m'))
numero2 = int(input('\033[mNumero 2: \033[32m'))

if numero1 > numero2:
    print('\033[31mO primeiro numero é \033[4mMAIOR!!\033[m')
elif numero1 == numero2:
    print('\033[31mOs numero são iguais.')
else:
    print('\033[31mO segundo valor é \033[4mMAIOR!!\033[m')
