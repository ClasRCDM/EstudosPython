print('{1}{0} Desafio 53 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

print('=' * 33)
print('{:^32}'.format('DETECTOR DE PALÍNDROMO'))
print('=' * 33)

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

'''for letras in range(len(junto) - 1, -1, -1):
    inverso += junto[letras]'''

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!!')
