from math import hypot
print('{0} Desafio 17 {0}'.format('=' * 10))
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
r = (c1 ** 2 + c2 ** 2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(r))
print('O comprimento da hipotenusa é {:.2f}'.format(hypot(c1, c2)))
