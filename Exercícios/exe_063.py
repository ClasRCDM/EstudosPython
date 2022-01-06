print('{1}{0} Desafio 63 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))
print('Sequencia de Fibonacci.\n')

N = int(input('Quantos termos você quer mostrar? '))

t1, t2 = 0, 1

print(f'{t1} > {t2}', end='')
cont = 3

while cont <= N:
    t3 = t1 + t2
    print(f' > {t3}', end='')

    t1 = t2
    t2 = t3

    cont += 1
else:
    print(' > FIM!')
