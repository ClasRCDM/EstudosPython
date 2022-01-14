print('{1}{0}{2}{3}'.format(f'{"_ Exercício 72 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    number = int(input('Digite um número. [0 a 20]: '))
    if number > 20 or number < 0:
        print('Tente novamente!')
        continue
    else:
        print(f'Você digitou o número {tupla[number]}.')
        break
