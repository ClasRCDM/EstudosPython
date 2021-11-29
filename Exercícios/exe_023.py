print('{0} Desafio 23 {0}'.format('=' * 10))

'''numero = int(input('Digite um numero entre[0 e 9999]: '))
numero = str(numero)

print(numero = int(input('Digite um numero entre[0 e 9999]: '))
numero = str(numero)

Dezena:{}
Centena:{}
Milhar:{}.format(numero[3],
                    numero[2],
                    numero[1],
                    numero[0]))'''

# Outra forma

numero = int(input('Digite um numero entre[0 e 9999]: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(u,
                     d,
                     c,
                     m))
