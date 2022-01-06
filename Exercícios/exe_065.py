print('{1}{0} Desafio 65 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

resp = 'S'
soma = quant = média = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))

    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
else:
    media = soma / quant

    print(f'Você digitou {quant} números e a média foi {media}')
    print(f'O maior valor foi {maior} e o menor foi {menor}')
