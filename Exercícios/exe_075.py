print('{1}{0}{2}'.format(f'{"_ Exercício 75 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m'))

tupla = tuple((
    int(input('Digite o primeiro número: ')),
    int(input('Digite o segundo número: ')),
    int(input('Digite o terceiro número: ')),
    int(input('Digite o quarto número: '))
))

print('Você digitou os valores', ' - '.join([str(numeros) for numeros in tupla]))
print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print('Os valores pares digitados foram, ', end='')
for n in tupla:
    if n % 2 == 0: print(n, end=' - ')
