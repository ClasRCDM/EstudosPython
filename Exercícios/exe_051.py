print('{1}{0} Desafio 51 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

print('=' * 33)
print('{:^32}'.format('10 TERMOS DE UMA PA'))
print('=' * 33)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão

for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' ➡️ ')
else:
    print('{}FIM{}'.format('\033[4;31m', '\033[m'))
