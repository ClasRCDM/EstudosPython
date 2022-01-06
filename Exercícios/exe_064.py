print('{1}{0} Desafio 64 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

num = cont = soma = 0
num = int(input('Dígite um número [999 para parar]: '))

while num != 999:
    soma += num
    cont += 1

    num = int(input('Dígite um número [999 para parar]: '))
else:
    print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
