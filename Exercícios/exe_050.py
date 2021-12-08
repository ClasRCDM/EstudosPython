print('{1}{0} Desafio 50 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

s = 0
números_descartados = list()

for números in range(7):
    n = int(input('Dígite número: '))
    if n % 2 == 0:
        s += n
    else:
        números_descartados.append(n)
else:
    print('A soma é {}'.format(s))
    print('Os numeros descartados foram \n{}'.format(números_descartados))
