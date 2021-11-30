from datetime import date

print('{1}{0} Desafio 39 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

ano = int(input('Qual ano você nasceu? \033[32m'))

ano_atual = date.today().year
idade = ano_atual - ano

if idade < 18:
    print('Você tem {} anos e ainda não necessita se alistar'.format(idade))
    print('Falta {} anos para se alistar'.format(18 - idade))
elif idade >= 18:
    print('Você tem que se alistar o mais rapido possivel')
    print('Devia ter se alistado a {} anos atrás'.format(idade - 18))
elif idade >= 65:
    print('Você não precisa se alistar mais')
