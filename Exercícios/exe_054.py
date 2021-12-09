from datetime import date

print('{1}{0} Desafio 54 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

atual = date.today().year

totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nasc

    if idade >= 21:
        print('Essa pessoa é maior')
        totmaior += 1
    else:
        print('Essa pessoa é menor')
        totmenor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))
