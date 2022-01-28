from datetime import date

print('{1}{0}{2}{3}'.format(f'{"_ Exercício 101 _":=^25}',
      '\033[4;33m<< ', ' >>\033[m', '\n'))


def voto(ano):
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade < 16: return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65: return f'Com {idade} anos: VOTO OPCIONAL.'
    else: return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# -

ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
