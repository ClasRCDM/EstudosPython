print('{1}{0}{2}'.format(f'{" Exercício 66 ":=^25}', '\033[4;33m', '\033[m'))

quant = soma = int(0)

while True:
    number = int(input('Digite um número: '))

    if number == 999:break

    quant += 1
    soma += number

print(f'Você digitou {quant} números e a soma dos mesmo é {soma}!')
