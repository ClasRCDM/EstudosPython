from math import radians, sin, cos, tan
print('{0} Desafio 18 {0}'.format('=' * 10))
an = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
print('O ãngulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tangente))
