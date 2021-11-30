from datetime import date

print('{1}{0} Desafio 41 {0}{2}'.format('=' * 10, '\033[4;33m', '\033[m'))

ano = int(input('Qual ano você nasceu? \033[32m'))

ano_atual = date.today().year
idade = ano_atual - ano

print('\033[36mSua idade é {}'.format(idade))

if idade <= 9:
    print('\033[30mVocê esta na categoria {}MIRIM{}!!'.format('\033[4m', '\033[m'))
elif idade <= 14:
    print('\033[30mVocê é da categoria {}INFANTIL{}!!'.format('\033[4m', '\033[m'))
elif idade <= 19:
    print('\033[30mVocê é um {}JUNIOR{}!!'.format('\033[4m', '\033[m'))
elif idade == 20:
    print('\033[30mParabéns você é um {}SÊNIOR{}!!'.format('\033[4m', '\033[m'))
else:
    print('\033[30mINCRIVEL VOCÊ È UM {}MASTER{}!!'.format('\033[4m', '\033[m'))
