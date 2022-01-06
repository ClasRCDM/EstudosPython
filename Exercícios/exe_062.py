print('{1}{0} Desafio 62 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

prim = int(input('Primeiro termo: '))
razão = int(input('Razão de PA: '))

termo = prim
cont = 1

total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} > ', end='')

        termo += razão
        cont += 1
    else:
        print('PAUSA')
        mais = int(input('\nQuantos termos você quer mostrar a mais? '))
else:
    print('FIM!!!')
