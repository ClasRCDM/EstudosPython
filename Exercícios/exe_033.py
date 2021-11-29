print('{0} Desafio 33 {0}'.format('=' * 10))

numero1 = int(input('Primeiro: '))
numero2 = int(input('Segundo: '))
numero3 = int(input('Terceiro: '))

maior = 0
menor = 0

if numero1 > numero2:
    maior = numero1
if numero2 > numero3:
    maior = numero2
if numero3 > numero1:
    maior = numero3

if numero1 < numero2:
    menor = numero1
if numero2 < numero3:
    menor = numero2
if numero3 < numero1:
    menor = numero3

print('O maior numero é {}\nO menor numero é {}'.format(maior, menor))
