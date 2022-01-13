print('{1}{0}{2}{3}'.format(
    f'{" Exercício 66 ":=^25}', '\033[4;33m', '\033[m', '\n'))

quant = soma = number = int(0)

while True:
    number, soma = int(input('Digite um número: ')), soma + number

    if number == 999: break

    quant += 1

print(f'Você digitou {quant} números e a soma dos mesmos é {soma}!')
